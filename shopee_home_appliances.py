from DrissionPage import ChromiumPage
import pandas as pd
import time
import os
from datetime import datetime

def extract_shopee_home_appliances():
    page = ChromiumPage()
    api_url = "api/v4/search/search_items"
    
    # 1. DANH SÁCH NHÓM ĐỒ GIA DỤNG
    categories = {
        "Kitchen-Appliances": "https://shopee.vn/Thiết-Bị-Điện-Gia-Dụng-Nhà-Bếp-cat.11036131.11036132?sortBy=sales",
        "Home-Care": "https://shopee.vn/Thiết-Bị-Chăm-Sóc-Nhà-Cửa-cat.11036131.11036133?sortBy=sales",
        "Air-Treatment": "https://shopee.vn/Thiết-Bị-Làm-Mát-Lọc-Không-Khí-cat.11036131.11036134?sortBy=sales",
        "Large-Appliances": "https://shopee.vn/Thiết-Bị-Gia-Dụng-Lớn-cat.11036131.11036135?sortBy=sales"
    }
    
    all_data = []
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M")

    try:
        print(f"--- Bắt đầu phiên cào Đồ Gia Dụng: {now.strftime('%d/%m/%Y %H:%M:%S')} ---")
        
        for group_name, base_url in categories.items():
            print(f"🚀 Đang cào nhóm: {group_name}...")
            
            for page_num in range(1): 
                target_url = f"{base_url}&page={page_num}"
                
                page.listen.start(api_url)
                page.get(target_url)
                
                res = page.listen.wait(timeout=15)
                if res and res.response and res.response.body:
                    # Fix lỗi NoneType ở đây
                    items = res.response.body.get('items')
                    
                    # Nếu items là None (Shopee không trả về danh sách), bỏ qua và đi tiếp
                    if not isinstance(items, list):
                        print(f"   ⚠️ Cảnh báo: Không lấy được danh sách sản phẩm (có thể do Shopee chặn bot). Bỏ qua trang này.")
                        continue

                    for i in items:
                        b = i.get('item_basic', i)
                        if b.get('itemid'):
                            raw_ctime = b.get('ctime')
                            f_create_time = datetime.fromtimestamp(raw_ctime).strftime("%Y-%m-%d %H:%M:%S") if raw_ctime else None
                            
                            # Đảm bảo rating_count không bị lỗi nếu cấu trúc trả về thay đổi
                            item_rating = b.get('item_rating')
                            rating_count_val = item_rating.get('rating_count')[0] if item_rating and item_rating.get('rating_count') else 0
                            rating_star_val = item_rating.get('rating_star') if item_rating else 0

                            all_data.append({
                                "analysis_group": group_name,
                                "item_id": b.get('itemid'),
                                "product_name": b.get('name'),
                                "price": b.get('price') / 100000 if b.get('price') else 0,
                                "rating_star": rating_star_val,
                                "rating_count": rating_count_val,
                                "monthly_sold": b.get('sold', 0),
                                "historical_sold": b.get('historical_sold', 0),
                                "shop_location": b.get('shop_location'),
                                "is_mall": b.get('is_official_shop', False),
                                "create_time": f_create_time,
                                "crawl_time": now.strftime("%Y-%m-%d %H:%M:%S")
                            })
                page.listen.stop()
                time.sleep(3) # Tăng thời gian nghỉ lên 3s để tránh bị block quá nhanh

        # 2. LƯU FILE
        if all_data:
            df = pd.DataFrame(all_data)
            output_file = f"Shopee_Home_Appliances_{timestamp_str}.xlsx"
            df.to_excel(output_file, index=False)
            print(f"\n✅ THÀNH CÔNG! Đã lưu file: {output_file}")
            print(f"📊 Tổng số sản phẩm thu thập: {len(df)}")
        else:
            print("\n❌ Không lấy được dữ liệu trong phiên này.")

    except Exception as e:
        print(f"💥 Lỗi không xác định: {e}")
    finally:
        page.quit()

if __name__ == "__main__":
    extract_shopee_home_appliances()