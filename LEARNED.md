# Thinks I leanred building NgonTinh Vault

## M1.1 - Pydantic Story Model

### Why dict[str, Story] instead of list[Story]?

Gợi ý cách suy nghĩ (không phải câu trả lời sẵn):
Nếu dùng list, để tìm story theo id em phải làm gì? Big-O complexity?
Nếu dùng dict, em làm gì? Big-O complexity?
Lúc nào em hay tìm story? Khi list ra hết, hay khi user gõ read trong-sinh 47?

====> 
- Nếu dùng list để tìm story theo ID thì sẽ phải chạy 2 lượt loop để tìm, Big-O = O(n)
- Nếu dùng dict thì chỉ cần tìm theo key, mapping với value để ra được truyện cần tìm. Big-O = O(1) 
- Mỗi lần gọi library.get(...), truyên vào ID. 
- Trong 7 command CLI (add, list, read, complete, drop, rate), command cần tìm story theo ID là: read, complete, drop, rate.

- Library sử dụng Dict bởi vì lookup-by-id là hành động phổ biến nhất. Ví dụ, khi user nhập "read Tam sinh tam the 47", chúng ta cần phải tìm truyện có ID "Tam sinh tam thế" để update current_chapter của nó.

- Trade-off: Dict không thể sort trực tiếp. Để có thể list tất cả các stories đã được sorted bởi rating, chúng ta phải chuyển sang dạng List trước thông qua "list(stories.values())".