# Things I leanred building NgonTinh Vault

## M1.1 - Pydantic Story Model

### Why dict[str, Story] instead of list[Story]?


====> 
Library sử dụng Dict bởi vì lookup-by-id là hành động phổ biến nhất.
Ví dụ, khi user nhập "read tam-sinh-tam-the 47", chúng ta cần phải tìm
truyện có id "tam-sinh-tam-the" để update current_chapter.

- dict lookup: O(1) — hash key, jump thẳng đến value. Thời gian không
  đổi dù có 10 hay 10000 truyện.
- list lookup: O(n) — phải loop qua từng truyện đến khi id khớp. Với
  500 truyện, chậm gấp 500 lần dict.

Trong 7 command CLI của Phase 1, 4 command (read, complete, drop, rate)
cần lookup-by-id trước khi update. Vì vậy dict pay off ngay từ Phase 1.

Trade-off: dict không sort trực tiếp được. Để list tất cả truyện sorted
theo rating, phải convert sang list trước qua `list(stories.values())`.
Nhưng sorting hiếm; lookup xảy ra mọi command. Dict thắng.