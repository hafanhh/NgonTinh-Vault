
import requests
def call_ollama(prompt: str) -> str:
    '''
    To send prompt, return string response
    '''
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json = payload)
        return response.json()['response']
    except requests.exceptions.ConnectionError:
        return "Ollama hasn't run. Please turn on app Ollama!"


if __name__ == "__main__":
    raw_text = '''
        Lữ Đề trong mắt trong trẻo rút đi, sóng mắt hơi chọn, đầu ngón tay câu lấy hắn vạt áo hệ mang, nhẹ nhàng kéo một chút, mang theo vài phần lưu luyến mị ý.

“Mỗi một ngày, đều tưởng.”

Hạng Võ ánh mắt chợt tối sầm đi xuống, cúi đầu, hôn lấy nàng môi.

Hắn hôn đến lại thâm lại cấp, một bàn tay nâng nàng cái gáy, ngón cái để ở nàng nhĩ sau kia phiến mềm mại làn da thượng, một cái tay khác từ nàng bên hông hoạt đi lên, mang theo vết chai mỏng lòng bàn tay cọ qua nàng tinh tế da thịt.

Lữ Đề bị hắn hôn đến hơi hơi ngửa ra sau, ngón tay nắm chặt hắn rộng mở cổ áo, móng tay cách vật liệu may mặc ở hắn xương quai xanh thượng nhẹ nhàng thổi qua, nghe thấy hắn từ yết hầu chỗ sâu trong phát ra một tiếng cực thấp kêu rên.

Hạng Võ buông ra nàng môi, cái trán vẫn chống cái trán của nàng, hô hấp thô nặng mà dồn dập.

Hắn lông mi cơ hồ quét đến nàng lông mi, mắt phượng cuồn cuộn không chút nào che lấp khao khát, lại ở nàng nhẹ suyễn khi dừng lại, khắc chế, chờ nàng bình phục.

Lữ Đề hơi hơi thở dốc, sóng mắt dạng đèn diễm quang, ngón tay không nhanh không chậm mà sờ soạng đến hắn vai giáp hệ khấu, một viên một viên thế hắn cởi bỏ.

Động tác cực nhẹ cực chậm, giống ở hủy đi một kiện chờ mong đã lâu lễ vật.

Hạng Võ cúi đầu, nhìn nàng tinh tế trắng nõn ngón tay, ở lạnh băng chiến giáp gian linh hoạt mà xuyên qua, phiên động như điệp.

Hắn đáy mắt ám lửa đốt đến càng vượng, trong thanh âm mang theo dày đặc dục cầu.

“A Nhu khi nào học được giải giáp.”

“Mỗi lần ngươi xuất chinh trở về đều phải giải, xem cũng xem biết.”

Lữ Đề đem cuối cùng một cái hệ khấu cởi bỏ, huyền giáp từ đầu vai chảy xuống, đánh vào sập biên mộc trên sàn nhà phát ra một tiếng nặng nề vang.

Nàng đẩy hắn ngực đem hắn đẩy ngã ở chăn gấm thượng, xoay người ngồi dậy, đầu ngón tay xoa hắn xương sườn bên một đạo tân thêm ứ thanh.

Kia ứ thanh từ xương sườn vẫn luôn lan tràn đến eo sườn, xanh tím đan xen, sấn Hạng Võ rắn chắc khẩn trí cơ bắp đường cong —— là trên chiến trường lưu lại ấn ký, cũng là tắm máu trở về huân chương.

Lữ Đề cúi đầu nhìn kỹ, bỗng nhiên cúi xuống thân, ở ứ thanh bên cạnh cực nhẹ cực nhẹ mà hôn một chút.

Hạng Võ ngón tay nháy mắt buộc chặt nàng eo sườn, hầu kết hung hăng lăn lộn, giống một đầu bị thuận mao mãnh thú, rõ ràng có thể xoay người đem nàng áp xuống.

Lại cố tình cam nguyện nằm ở nơi đó, nhậm nàng dùng ngón tay một tấc một tấc đo đạc trên người hắn mỗi một đạo vết thương.

“A Nhu ——”

Hạng Võ thấp thấp gọi nàng một tiếng, duỗi tay nắm lấy nàng eo, đem nàng một lần nữa mang nhập trong lòng ngực.

Nàng thuận thế cúi xuống thân, môi gần sát hắn bên tai, thanh âm nhẹ đến giống lông chim phất quá vành tai, mang theo một tia như có như không ý cười.

“A Vũ, ngươi mỗi một lần chiến thắng trở về, ta đều ở.”

Hạng Võ trả lời là một cái càng sâu hôn.

Hai người cùng nhau chìm vào chăn gấm.

Đèn diễm ở trướng ngoại nhẹ nhàng nhảy nhảy, ai cũng không có lại đi quản nó.

……

Qua thật lâu, Hạng Võ dựa vào nàng phía sau, đem nàng vòng ở trong ngực.

Cánh tay hắn từ nàng bên hông vòng qua, cằm gác ở nàng hõm vai, hô hấp đã vững vàng xuống dưới.

Lữ Đề bối dán hắn ngực, ngón tay có một chút không một chút mà vòng quanh hắn đuôi tóc.

Hạng Võ an tĩnh mà nhậm nàng đùa nghịch, trong cổ họng phát ra một tiếng cực nhẹ cực thỏa mãn than thở.

“Đúng rồi.”

Hắn bỗng nhiên nhớ tới cái gì, ngẩng đầu, cằm gác ở nàng trên vai, đôi mắt lại sáng lên.

“Ngươi có nhớ hay không, chiến trước ngươi cùng ta đề qua cái kia bộ tốt —— sườn núi thượng khám định đào thế cục, còn nói đãi ngày sau kiến công lại tưởng cáo tên họ? Vây yển, chính là hắn dẫn người quật.

Ta ở sườn núi thượng xa xa nhìn hắn liếc mắt một cái, cách xa nhau mấy trăm bước, thấy không rõ khuôn mặt, nhưng bằng kia thân lỗi lạc khí phách, liền biết nhất định là hắn.”

Hạng Võ dừng một chút, đem Lữ Đề tay cầm trong lòng bàn tay, ngón cái ở nàng mu bàn tay thượng nhẹ nhàng vuốt ve.

“A Nhu, ngươi lúc trước liếc mắt một cái liền nhìn thấu hắn binh lược tài học. Này phân ánh mắt, hơn xa với ta.”

Lữ Đề xoay người xem hắn, sóng mắt trong trẻo, dạng trứ nhiên tự đắc chắc chắn.

Hàn Tín.

Ngày ấy sườn núi thượng, hắn liền tên họ cũng không dám thổ lộ, chỉ để lại một câu “Đãi ngày sau kiến công, lại làm tiên sinh biết được”.

Mà nay, hắn rốt cuộc muốn ở nàng trước mặt, đường đường chính chính báo ra tên họ.

“Không phải ta ánh mắt chuẩn. Là hắn ở sườn núi thượng suy đoán sách luận khi, câu câu chữ chữ đều dừng ở thật chỗ, tưởng tàng cũng tàng không được.”

Lữ Đề cong cong khóe môi.

“Ngươi đem quật yển người tìm được rồi, hắn tên gọi là gì?”

“Hàn Tín.” Hạng Võ đem tay nàng chỉ khấu tiến chính mình chỉ gian, lòng bàn tay dán lòng bàn tay.

“Ta còn chưa kịp triệu hắn, một lòng chỉ nghĩ chạy như bay trở về gặp ngươi.

A Nhu, hắn là ngươi trước hết nhận biết người, ngày mai chúng ta cùng đi gặp hắn. Vây yển phóng thủy này phân công lớn, cũng nên từ ngươi vị này tuệ nhãn thức mới tiên sinh, chính miệng tán hắn.”

Lữ Đề khóe môi hơi câu, rũ mắt nhìn về phía hai người giao nắm tay.

Hạng Võ đốt ngón tay thô lệ, tay nàng chỉ tinh tế, bị hắn chặt chẽ khấu ở lòng bàn tay, giống như một đoạn bị thích đáng cất chứa bạch ngọc.

Nàng đầu ngón tay nhẹ nhàng tiền boa, quấn lên hắn chỉ.

“Hảo.”

Lữ Đề nhẹ nhàng gật gật đầu, đáy mắt xẹt qua một sợi ám quang.

“Ta cũng muốn nhìn xem, trên chiến trường quật yển người, cùng sườn núi thượng suy đoán khi có cái gì không giống nhau.

Xem hắn hay không, còn tàng được đôi mắt nóng rực.

Lữ Đề nâng lên mắt, đèn diễm ở nàng con ngươi nhẹ nhàng nhảy một chút.

Thanh minh hai tròng mắt, chiếu ra Hạng Võ mãn hàm tình yêu ảnh ngược, cùng một mâm chưa xong ván cờ.
    '''
    
    prompt = f"Hãy tóm tắt đoạn truyện sau bằng tiếng Việt, ngắn gọn 2-3 câu:\n\n{raw_text}"
    print(call_ollama(prompt))
    
    
    