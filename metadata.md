# Metadata: Shopee Home Appliances Dataset

## 1. Thông tin chung (General Information)
* **Dự án:** Phân tích dữ liệu thương mại điện tử Shopee.
* **Người thực hiện:** Nguyễn Bảo Long.
* **Mục tiêu:** Thu thập dữ liệu đồ gia dụng để thực hiện phân tích thị trường, phân khúc khách hàng và hành vi mua sắm.
* **Nguồn dữ liệu:** Shopee Việt Nam (thông qua công cụ cào dữ liệu tự động).
* **Định dạng file:** `.xlsx`, `.csv`.

---

## 2. Mô tả các trường dữ liệu (Data Dictionary)

| Tên cột | Kiểu dữ liệu | Mô tả chi tiết | Ghi chú |
| :--- | :--- | :--- | :--- |
| **analysis_group** | String | Nhóm phân loại sản phẩm. | Các nhóm: Kitchen, Home-Care, Air-Treatment, Large-Appliances. |
| **item_id** | Integer | Mã định danh duy nhất của sản phẩm trên hệ thống Shopee. | Dùng làm khóa chính (Primary Key). |
| **product_name** | String | Tên hiển thị của sản phẩm. | Dùng cho phân tích từ khóa hoặc Sentiment Analysis. |
| **price** | Float | Giá bán của sản phẩm sau khi đã quy đổi đơn vị. | Đơn vị: VNĐ. |
| **rating_star** | Float | Điểm đánh giá trung bình từ người mua (thang điểm 5). | Chỉ số chất lượng sản phẩm. |
| **rating_count** | Integer | Tổng số lượt khách hàng đã để lại đánh giá. | Phản ánh độ uy tín và tương tác. |
| **monthly_sold** | Integer | Số lượng sản phẩm bán ra trong 30 ngày gần nhất. | Chỉ số phản ánh sức nóng hiện tại. |
| **historical_sold** | Integer | Tổng số lượng sản phẩm đã bán từ khi đăng bài. | Đánh giá vòng đời sản phẩm. |
| **shop_location** | String | Địa chỉ tỉnh/thành phố nơi kho hàng của shop tọa lạc. | Phân tích địa lý nhà cung cấp. |
| **is_mall** | Boolean | Xác định sản phẩm thuộc gian hàng chính hãng (Shopee Mall). | `True`: Mall, `False`: Shop thường. |
| **create_time** | DateTime | Thời gian sản phẩm bắt đầu được đăng bán. | Định dạng: `YYYY-MM-DD HH:MM:SS`. |
| **crawl_time** | DateTime | Thời điểm thực hiện thu thập dữ liệu. | Dùng để quản lý tính cập nhật của dữ liệu. |

---

## 3. Hướng dẫn sử dụng (Usage)
Dữ liệu này có thể được sử dụng cho các bài toán:
1. **Descriptive Statistics:** Thống kê mô tả thị trường đồ gia dụng.
2. **Clustering:** Phân cụm sản phẩm dựa trên giá và sức bán (K-Means).
3. **Correlation Analysis:** Phân tích mối tương quan giữa điểm đánh giá (rating) và doanh số.

---
*Cập nhật lần cuối: 29/03/2026*