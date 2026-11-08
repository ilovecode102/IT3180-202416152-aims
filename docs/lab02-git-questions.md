1\. Vì sao phải đồng bộ main trước khi tạo Pull Request?



Đồng bộ main giúp branch hiện tại cập nhật những thay đổi mới nhất từ các thành viên khác, đồng thời phát hiện và xử lý conflict sớm. Nhờ đó, code được kiểm thử trên phiên bản mới nhất và giảm rủi ro khi merge PR.



2\. Khi nào không nên sử dụng rebase?



Không nên rebase các branch đã được chia sẻ và đang có người khác sử dụng, vì rebase viết lại lịch sử commit và có thể gây xung đột cho những người cộng tác. Ngoài ra, không nên rebase main hoặc các branch dùng chung khi cần bảo toàn lịch sử tích hợp.



3\. feature/\* khác topic/\* như thế nào?



feature/\* thường dùng cho việc phát triển chức năng mới của ứng dụng, còn topic/\* thường dùng cho một nhiệm vụ cụ thể như tài liệu, refactoring hoặc cấu hình. Đây chỉ là quy ước đặt tên, Git không phân biệt hai loại branch này về mặt kỹ thuật.

