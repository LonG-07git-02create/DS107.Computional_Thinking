# Link của bộ dataset : https://www.kaggle.com/datasets/atomicd/retail-store-inventory-and-demand-forecasting
# Miêu tả bộ dữ liệu

1. Date: Trục thời gian. Cho phép mô hình hóa tính tự tương quan (autocorrelation). Dữ liệu bán lẻ thường có tính chu kỳ theo tuần (xác suất mua sắm cuối tuần cao hơn).
2. Store ID & Product ID: Các biến định danh giúp mô hình học được đặc tính riêng biệt của từng cửa hàng (ví dụ: cửa hàng quy mô lớn) hoặc từng mặt hàng (ví dụ: mặt hàng thiết yếu vs. xa xỉ).
3. Category: Giúp nhóm các sản phẩm có cùng hành vi tiêu dùng. Các sản phẩm cùng loại thường có chung độ co giãn của cầu theo giá.
4. Region: Đại diện cho yếu tố địa lý. Mỗi vùng miền có một "phân phối hành vi" khác nhau (ví dụ: miền Bắc mua đồ mùa đông nhiều hơn miền Nam).
5. Inventory Level (Mức tồn kho): Cho biết số lượng hàng sẵn có. Đây là "ngưỡng chặn" trên của Units Sold. Nếu tồn kho bằng 0, doanh số sẽ bằng 0 bất kể nhu cầu thực tế cao bao nhiêu.
6. Units Sold (Đã bán): Giá trị thực tế quan sát được (observed value). Trong thống kê, đây là một biến rời rạc thường tuân theo phân phối Poisson.
7. Units Ordered (Hàng đặt thêm): Phản ánh chiến lược tái cung ứng. Biến này thường có độ trễ (lag) so với Demand.
8. Price (Giá): Biến số quyết định. Theo luật cung cầu, nhu cầu thường có tỷ lệ nghịch với giá.
9. Discount (Giảm giá): Tác động trực tiếp đến kỳ vọng của khách hàng. Giảm giá làm thay đổi hàm phân phối của nhu cầu, đẩy xác suất bán được hàng cao hơn về phía các giá trị lớn.
10. Competitor Pricing (Giá đối thủ): Một biến hiệp biến (covariate). Nếu $Price > Competitor\_Pricing$, xác suất khách hàng rời bỏ (churn) tăng lên. Đây là yếu tố gây nhiễu quan trọng trong các mô hình dự báo.
11. Promotion (Khuyến mãi): Biến giả (dummy variable) thể hiện sự can thiệp có chủ đích. Nó thường tạo ra các "điểm đột biến" (spikes) trong dữ liệu thời gian.
12. Weather Condition: Thời tiết tác động đến tâm lý và khả năng di chuyển. Ví dụ: Trời mưa làm giảm xác suất khách đến cửa hàng trực tiếp nhưng có thể tăng nhu cầu đặt hàng online.
13. Seasonality (Mùa vụ): Đại diện cho các biến động lặp lại. Nó giúp tách biệt giữa "xu hướng tăng trưởng thực" và "tăng trưởng do đến mùa".
14. Epidemic (Dịch bệnh): Một biến cố hiếm (rare event) nhưng có tác động cực lớn. Về mặt thống kê, nó gây ra sự thay đổi cấu trúc (structural break) trong chuỗi dữ liệu, khiến các quy luật cũ có thể không còn đúng.
15. Demand (Nhu cầu): Đây là giá trị cần dự báo. Khác với Units Sold (chỉ ghi lại những gì đã diễn ra), Demand là nhu cầu thực sự của thị trường (bao gồm cả những khách muốn mua nhưng không có hàng). Trong Machine Learning, đây thường là biến mà ta dùng để tối ưu hóa hàm mất mát (Loss Function).


- Các phương pháp để kiểm tra sự tương tác lẫn nhau giữa các mặt hàng 

1. Sử dụng thống kê thuần túy: 
Kiểm định Chi-square (Chi-square Test for Independence):

Cách làm: Lập một bảng (Contingency Table) đếm số lần (Điện tử có, Đồ chơi có), (Điện tử có, Đồ chơi không), v.v.


Chỉ số Lift (Độ nâng) trong Association Rules:

2. Sử dụng machine learning: 

- Phân cụm (Clustering)
GMM giả định mỗi cụm là một phân phối chuẩn đa biến. Nó sẽ tìm ra các nhóm Store/Ngày mà ở đó phân phối nhu cầu của nhiều mặt hàng (Electronics, Toys, Groceries) dịch chuyển cùng nhau.

Bạn phát hiện ra "Nhóm cửa hàng gia đình" (có nhu cầu Toys & Groceries cao) khác với "Nhóm cửa hàng công nghệ".


