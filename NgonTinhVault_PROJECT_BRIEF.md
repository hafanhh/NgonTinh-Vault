# 🌸 NgônTình Vault

> **Personal Reading Companion for Ngôn Tình Readers**
> Mini-project · 4 tuần · Python + Ollama
> "Vì đọc 5 truyện song song mà không quên plot là một kỹ năng — và app này biến nó thành reality"

---

## 🎯 Vision: Em sẽ build được cái gì?

Một app chạy trên terminal — quản lý toàn bộ life truyện ngôn tình của em. Cuối project, lúc demo, em sẽ chạy `python main.py` và thấy:

```
╔══════════════════════════════════════════════════════════════╗
║              🌸 NGÔN TÌNH VAULT 🌸                            ║
║         "Your reading life, organized"                        ║
╚══════════════════════════════════════════════════════════════╝

📚 Đang đọc (3):
  ▸ Trọng Sinh Chi Đích Nữ Hoàn Kinh        Chap 47/200  📍
  ▸ Em Là Một Cô Gái Ngọt Ngào              Chap 12/85   📍
  ▸ Hôn Nhân Hợp Đồng Với Tổng Tài          Chap 23/60   📍

🎯 Top TBR (5 truyện hợp mood "ngọt sủng + niên hạ"):
  1. ⭐ 4.8 · Cô Vợ Nhỏ Của Boss Hắc Đạo    [niên hạ, hắc bang, HE]
  2. ⭐ 4.7 · Anh Trai Nuôi Dạy Em           [niên hạ, ngọt sủng, 1v1]
  ...

> recap "Trọng Sinh Chi Đích Nữ" 5
[AI đang tóm tắt 5 chapter gần nhất...]

📖 Tóm tắt chap 43-47:
   Tô Lan trở về phủ thừa tướng sau khi phát hiện
   Diệp Khả Tâm thật ra là người đã hại nàng kiếp trước.
   Lần này nàng quyết định không cứu Diệp nữa, mà...
   [continues...]

> _
```

Đây là endgame. Nhưng cái thật sự sướng là: **bạn ấy sẽ DÙNG nó**. Mỗi tối đọc xong chapter, paste vào, AI tóm tắt, lưu lại. Sau 1 tháng có một database cá nhân về toàn bộ truyện đã đọc. Không một app commercial nào ở VN làm được cái này đúng way bạn ấy cần.

---

## 🤔 Tại sao project này phù hợp với em?

| Em đang có | Project sẽ dạy em |
|---|---|
| ✅ DSA, Algorithms | Apply **Trie** (tag autocomplete), **Inverted Index** (search trong truyện), **Graph** (truyện similar), **Priority Queue** (TBR ranking) — tất cả trên data thật của em |
| ❌ OOP | Model một library system buộc em phải dùng Class, Composition. Domain (truyện, chapter, tag) ánh xạ tự nhiên ra OOP |
| ❌ Software dev | Cấu trúc project, Git, virtual env, testing, CLI design, JSON persistence, modular architecture |
| ❌ AI/LLM | Tích hợp Ollama, prompt engineering cho task tóm tắt/phân loại/extract — đây là 80% công việc của AI Engineer thật ngoài đời |
| 😴 Đang chán | Đây là project em sẽ thực sự DÙNG. Mỗi feature add vào là một thứ life em được nâng cấp. |

**Quan trọng:** Project này được thiết kế để cuối Phase 1 đã có cái em dùng được — chỉ là chưa có AI. Mỗi Phase đều ship được một version dùng thật.

---

## 🛠️ Tech Stack

| Tool | Version | Để làm gì |
|---|---|---|
| Python | 3.10+ | Ngôn ngữ chính |
| Ollama | latest | LLM ở local, miễn phí |
| `qwen2.5:3b` | - | **Recommend mạnh** — model tiếng Việt tốt nhất ở tier 3B |
| `llama3.2:3b` | - | Backup, English mạnh hơn nhưng tiếng Việt hơi yếu |
| `requests` | - | Gọi Ollama API |
| `rich` | - | Terminal UI đẹp (panel, table, color) |
| `pydantic` | v2 | Data validation cho models |
| `pytest` | - | Unit test |
| `black` + `ruff` | - | Code formatting & linting |

> 💡 **Lưu ý quan trọng về model:** Vì truyện ngôn tình tiếng Việt, em **phải** dùng model có Chinese/Vietnamese support tốt. **`qwen2.5:3b` là lựa chọn tốt nhất** ở size nhỏ (Qwen được train heavy trên Chinese, Vietnamese OK). Llama 3B sẽ tóm tắt tiếng Anh tốt nhưng tiếng Việt hơi awkward.

---

## 📐 Kiến trúc tổng thể

```
ngontinh-vault/
├── README.md
├── pyproject.toml
├── requirements.txt
├── main.py                    # entry point
│
├── ngontinh/
│   ├── __init__.py
│   ├── core/                  # Domain logic — KHÔNG biết LLM hay UI
│   │   ├── models.py          # Story, Chapter, Tag, ReadingStatus
│   │   ├── library.py         # Library — quản lý collection
│   │   ├── search.py          # Trie cho tag, Inverted index cho text
│   │   ├── recommender.py     # Graph-based "truyện similar"
│   │   └── tbr.py             # TBR list với priority queue
│   │
│   ├── ai/                    # LLM integration
│   │   ├── ollama_client.py   # Wrapper Ollama API
│   │   ├── summarizer.py      # Tóm tắt chapter
│   │   ├── tagger.py          # Auto-suggest tag
│   │   ├── extractor.py       # Extract nhân vật, địa điểm
│   │   └── prompts.py         # Prompt templates
│   │
│   ├── persistence/
│   │   └── repository.py      # Save/load JSON
│   │
│   └── ui/
│       ├── renderer.py        # In ra màn hình bằng rich
│       └── commands.py        # Parse "add story", "recap 5", ...
│
├── data/
│   └── library.json           # Database thật của em
│
└── tests/
    ├── test_models.py
    ├── test_search.py         # Test Trie + Inverted index
    ├── test_recommender.py
    └── test_tbr.py
```

**Nguyên tắc thiết kế quan trọng:** `core/` không được import gì từ `ai/` hay `ui/`. Domain logic phải độc lập với infrastructure. Lợi ích: test core không cần gọi LLM, không cần render UI → test nhanh, ổn định, isolated.

---

## 🗺️ Roadmap — 4 Phase, mỗi phase ship được

### 📅 Phase 0: Setup (1-2 ngày)

**Mục tiêu:** Có môi trường dev sẵn sàng, hello-world chạy được Ollama tiếng Việt.

#### Checklist:

- [ ] Cài Python 3.10+ (`python --version`)
- [ ] Tạo virtual env: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
- [ ] Cài Ollama từ https://ollama.com
- [ ] Pull model: `ollama pull qwen2.5:3b` (~2GB)
- [ ] Test Ollama tiếng Việt: `ollama run qwen2.5:3b "Tóm tắt: Một cô gái xuyên không về thời cổ đại, gặp thái tử lạnh lùng..."` — phải thấy nó respond OK tiếng Việt
- [ ] `git init`, `.gitignore` (ignore `venv/`, `__pycache__/`, `data/library.json` — vì là personal data)
- [ ] Tạo cấu trúc folder
- [ ] Viết `main.py` đầu tiên: paste 1 đoạn description truyện vào, AI tóm tắt ra

#### Code mẫu cho Phase 0:

```python
import requests

def summarize(text: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": f"Hãy tóm tắt đoạn truyện sau bằng tiếng Việt, ngắn gọn 2-3 câu:\n\n{text}",
            "stream": False
        }
    )
    return response.json()["response"]

if __name__ == "__main__":
    text = """
    Tô Lan mở mắt ra, phát hiện mình đã trở về thời điểm 5 năm trước,
    lúc nàng còn chưa gặp Tần Mạc. Nàng nhớ rõ kiếp trước Diệp Khả Tâm
    đã hại nàng thế nào, khiến nàng chết trong ngục thất...
    """
    print(summarize(text))
```

**Definition of Done:** Chạy `python main.py` → thấy tóm tắt tiếng Việt OK. Commit `chore: project setup`.

> 💡 **Self-check:** Nếu output toàn tiếng Anh hoặc tiếng Việt sai chính tả nhiều → model em đang dùng không phù hợp. Quay lại confirm `qwen2.5:3b` chứ không phải `llama3.2:3b`.

---

### 📅 Phase 1: Core OOP — Library Management (Tuần 1)

**Mục tiêu:** Có app chạy được — add truyện, list truyện, tag truyện, đánh dấu chapter đang đọc. **CHƯA có LLM, CHƯA có search xịn.**

#### Học được gì:
- Class, instance, `__init__`, `__repr__`
- Composition (`Library` HAS-A list of `Story`, `Story` HAS-A list of `Chapter`)
- Encapsulation (`_status` private, expose qua property)
- Type hints (`def add_story(self, story: Story) -> None`)
- Pydantic Model — validation tự động
- Enum (`ReadingStatus.READING`, `.COMPLETED`, `.DROPPED`, `.PLAN_TO_READ`)
- Tổ chức code thành module
- JSON serialization

#### Yêu cầu chức năng:

1. Thêm truyện: `add` → prompt nhập tên, tác giả, tags, link, total_chapters
2. List: `list` → in ra table tất cả truyện
3. Filter: `list reading`, `list completed`, `list tbr`
4. Update progress: `read <story_id> <chapter>` — đánh dấu đã đọc đến chap X
5. Status change: `complete <story_id>`, `drop <story_id>`, `rate <story_id> <1-5>`
6. Tag system: mỗi truyện có nhiều tag (cường thượng, niên hạ, HE, ...)
7. **Persistence**: tất cả lưu vào `data/library.json`, restart app thì còn nguyên
8. Có ít nhất 10 truyện sample (em tự nhập truyện em đã/đang đọc, đó là feature, không phải bug 😄)

#### Class design gợi ý:

```python
# core/models.py
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class ReadingStatus(str, Enum):
    PLAN_TO_READ = "plan_to_read"
    READING = "reading"
    COMPLETED = "completed"
    DROPPED = "dropped"
    ON_HOLD = "on_hold"

class Story(BaseModel):
    id: str                              # ví dụ: "trong-sinh-chi-dich-nu"
    title: str
    author: Optional[str] = None
    tags: list[str] = []                 # ["cường thượng", "trọng sinh", "HE"]
    total_chapters: Optional[int] = None
    current_chapter: int = 0
    status: ReadingStatus = ReadingStatus.PLAN_TO_READ
    rating: Optional[float] = None       # 0-5
    notes: str = ""
    chapter_summaries: dict[int, str] = {}  # {47: "Tô Lan phát hiện..."}
    added_at: datetime = Field(default_factory=datetime.now)
    last_read_at: Optional[datetime] = None
    
    @property
    def progress_percent(self) -> float:
        if not self.total_chapters:
            return 0.0
        return (self.current_chapter / self.total_chapters) * 100
    
    @property
    def is_finished(self) -> bool:
        return self.status == ReadingStatus.COMPLETED


# core/library.py
class Library:
    def __init__(self):
        self._stories: dict[str, Story] = {}    # hash map cho O(1) lookup
    
    def add(self, story: Story) -> None:
        if story.id in self._stories:
            raise ValueError(f"Story {story.id} already exists")
        self._stories[story.id] = story
    
    def get(self, story_id: str) -> Optional[Story]:
        return self._stories.get(story_id)
    
    def filter_by_status(self, status: ReadingStatus) -> list[Story]:
        return [s for s in self._stories.values() if s.status == status]
    
    def filter_by_tag(self, tag: str) -> list[Story]:
        return [s for s in self._stories.values() if tag in s.tags]
    
    def __len__(self) -> int:
        return len(self._stories)
    
    def __iter__(self):
        return iter(self._stories.values())
```

#### Bài tập tự suy nghĩ:

> 💡 **Câu hỏi 1:** Tại sao mình dùng `dict[str, Story]` cho `_stories` thay vì `list[Story]`? Hint: nghĩ về complexity của `library.get("xxx-id")`.

> 💡 **Câu hỏi 2:** `Chapter` có nên là class riêng hay chỉ là số `int` trong `current_chapter`? Trade-off?

#### Definition of Done Phase 1:

- [ ] Chạy `python main.py` thấy CLI
- [ ] Add 10 truyện em đang/đã đọc thật (đây là dataset thật, em sẽ dùng tới Phase 4)
- [ ] List, filter by status, filter by tag đều hoạt động
- [ ] Progress tracking hoạt động (đọc đến chap 47/200 hiển thị 23.5%)
- [ ] Save & load — tắt app, mở lại, data còn nguyên
- [ ] **Ít nhất 5 unit test** cho `Library` (add duplicate, get not exist, filter, ...)
- [ ] `ruff check .` không error
- [ ] Git có ít nhất 5 commit nhỏ với message rõ

> 🎉 **Khi xong Phase này, em đã có một Notion-lite cho ngôn tình.** Em có thể dùng nó hàng ngày luôn.

---

### 📅 Phase 2: Search & Discovery — DSA Thực Chiến (Tuần 2)

**Mục tiêu:** Thêm search xịn (Trie + Inverted Index), đề xuất truyện similar (Graph), TBR list với scoring (Priority Queue). Đây là phase mà DSA của em PAY OFF nặng nhất.

#### Học được gì:
- Apply **Trie** vào tag autocomplete
- Apply **Inverted Index** vào full-text search
- Apply **Graph** (bipartite: Story ↔ Tag) vào "truyện tương tự"
- Apply **Priority Queue (heap)** vào TBR ranking
- **Inheritance**: nhiều loại "Searcher" (TagSearcher, TextSearcher) cùng interface
- Performance thinking: O(n) vs O(log n) khi data scale

#### Yêu cầu:

##### 2.1 Tag Autocomplete với Trie

Khi em gõ `c` → suggest `cường thượng, cường công, cường cường, cung đấu, ...`. 
Khi gõ `cườ` → narrow xuống `cường thượng, cường công, cường cường`.

**Tại sao Trie?** Hash map không làm được prefix search. Em có thể duyệt list rồi `startswith()` — O(n×m). Trie cho em O(m) với m là độ dài prefix. Với 100 tag thì khác biệt nhỏ, với 10000 tag (sau khi em add tag từ 500 truyện) thì khác biệt lớn.

```python
# core/search.py
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.count: int = 0          # số truyện có tag này

class TagTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, tag: str) -> None:
        # implement
        ...
    
    def autocomplete(self, prefix: str, limit: int = 10) -> list[str]:
        # Trả về list các tag bắt đầu bằng prefix, sắp xếp theo count giảm dần
        ...
```

##### 2.2 Full-text Search với Inverted Index

Em muốn search "đông phương" trong toàn bộ description, summary, notes của tất cả truyện.

**Naive approach:** loop qua từng story, search trong từng field. O(n × m).
**Inverted Index:** preprocessing tạo map `{word: [story_id1, story_id2, ...]}`. Query O(1) per word.

```python
class InvertedIndex:
    def __init__(self):
        self._index: dict[str, set[str]] = {}    # word -> set of story_ids
    
    def add_story(self, story: Story) -> None:
        text = f"{story.title} {' '.join(story.tags)} {story.notes}"
        for word in self._tokenize(text):
            self._index.setdefault(word, set()).add(story.id)
    
    def search(self, query: str) -> set[str]:
        # AND search: tất cả từ trong query phải xuất hiện
        words = self._tokenize(query)
        if not words:
            return set()
        result = self._index.get(words[0], set()).copy()
        for word in words[1:]:
            result &= self._index.get(word, set())
        return result
    
    def _tokenize(self, text: str) -> list[str]:
        # Đơn giản: lowercase, tách space, loại stopwords
        # Bonus: dùng underthesea cho tokenization tiếng Việt xịn hơn
        ...
```

##### 2.3 Similar Stories với Graph

Truyện similar = chia sẻ nhiều tag chung. Đây là **bipartite graph**: một bên là Story, một bên là Tag, edge khi story có tag đó.

Similarity giữa 2 story = **Jaccard similarity** = |tags chung| / |tags hợp|.

```python
class SimilarityRecommender:
    def __init__(self, library: Library):
        self.library = library
    
    def find_similar(self, story_id: str, top_k: int = 5) -> list[tuple[Story, float]]:
        target = self.library.get(story_id)
        if not target:
            return []
        
        target_tags = set(target.tags)
        scores = []
        for other in self.library:
            if other.id == story_id:
                continue
            other_tags = set(other.tags)
            if not target_tags or not other_tags:
                continue
            jaccard = len(target_tags & other_tags) / len(target_tags | other_tags)
            if jaccard > 0:
                scores.append((other, jaccard))
        
        # Sort theo score giảm dần, lấy top k
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
```

> 💡 **Bonus thinking:** Với 50 truyện thì O(n) loop OK. Với 5000 thì sao? (Hint: index ngược tag → story_ids, chỉ duyệt qua story share ít nhất 1 tag).

##### 2.4 TBR Ranking với Priority Queue

Em có 30 truyện trong status PLAN_TO_READ. Đọc cái nào trước?

Score = `f(rating_avg_của_tag, độ_dài_phù_hợp_mood, độ_mới, ...)`. Mỗi tuần em update score, top được suggest đầu tiên.

```python
import heapq

class TBRRanker:
    def __init__(self, library: Library, mood_tags: list[str]):
        self.library = library
        self.mood_tags = mood_tags          # ["ngọt sủng", "niên hạ"]
    
    def top_n(self, n: int = 5) -> list[Story]:
        heap: list[tuple[float, str]] = []   # (-score, story_id) — min-heap dùng làm max-heap
        for story in self.library.filter_by_status(ReadingStatus.PLAN_TO_READ):
            score = self._score(story)
            heapq.heappush(heap, (-score, story.id))
        
        result = []
        for _ in range(min(n, len(heap))):
            _, story_id = heapq.heappop(heap)
            result.append(self.library.get(story_id))
        return result
    
    def _score(self, story: Story) -> float:
        tag_match = len(set(story.tags) & set(self.mood_tags))
        rating_bonus = (story.rating or 3.0) / 5.0
        # tự design công thức
        return tag_match * 2 + rating_bonus
```

#### Definition of Done Phase 2:

- [ ] Command `tag <prefix>` autocomplete tag (instant, không lag dù 1000 tag)
- [ ] Command `search <query>` tìm full-text trong title/tags/notes
- [ ] Command `similar <story_id>` đề xuất 5 truyện tương tự
- [ ] Command `tbr [mood1 mood2]` đề xuất top 5 truyện nên đọc
- [ ] **Ít nhất 10 unit test** (test Trie operations, Inverted index, Jaccard similarity, TBR ranking)
- [ ] **Benchmark**: viết file `benchmark.py` so sánh naive search vs inverted index trên 1000 truyện fake. Em sẽ thấy với mắt thường sự khác biệt.
- [ ] Refactor code Phase 1 nếu thấy class nào "biết quá nhiều"

> 🔥 **Đây là phase em sẽ thực sự thấy DSA có ích.** Nhiều người học DSA xong forget vì không apply. Em làm xong phase này là kiến thức trong xương rồi.

---

### 📅 Phase 3: AI Wakes Up — LLM Integration (Tuần 3)

**Mục tiêu:** Cho AI làm những thứ chỉ AI làm được — tóm tắt, gợi ý tag, extract nhân vật. Đây là phase "wow" mà bạn ấy sẽ flex được với hội bạn cùng đọc.

#### Học được gì:
- Design pattern: **Adapter** (wrap Ollama API thành interface mình control)
- Prompt engineering cho từng task khác nhau (summarize vs classify vs extract)
- **Structured output** từ LLM (parse JSON response)
- **Streaming response** (in từng từ ra giống ChatGPT)
- Conversation history & context window management
- Error handling: Ollama down? Response không phải JSON? Quá dài?
- **Caching** kết quả LLM (DP-style memoization — gọi LLM tốn thời gian, đừng gọi lại nếu đã có)

#### Yêu cầu:

##### 3.1 OllamaClient — Foundation

```python
# ai/ollama_client.py
from abc import ABC, abstractmethod
from typing import Iterator

class LLMClient(ABC):
    """Interface — code mình chỉ phụ thuộc cái này."""
    @abstractmethod
    def generate(self, prompt: str, system: str = "", json_mode: bool = False) -> str: ...
    @abstractmethod
    def stream(self, prompt: str, system: str = "") -> Iterator[str]: ...

class OllamaClient(LLMClient):
    def __init__(self, model: str = "qwen2.5:3b", host: str = "http://localhost:11434"):
        self.model = model
        self.host = host
    
    def generate(self, prompt, system="", json_mode=False):
        ...
```

> 🎓 **Tại sao tách abstract & concrete?** Mai mốt em muốn switch sang OpenAI, hay viết mock cho test (không gọi LLM thật) — em chỉ cần thay class implement, không sửa code khác. Đây là **Dependency Inversion Principle**. Em sẽ hiểu sâu khi viết test ở phase này.

##### 3.2 Chapter Summarizer — Feature flagship

Workflow:
1. Em paste raw text của 1 chapter (5000-15000 chữ)
2. App split chunk nếu quá dài
3. AI tóm tắt từng chunk → AI tóm tắt tổng hợp
4. Lưu summary vào `story.chapter_summaries[chapter_num]`
5. Cache: nếu chapter đã có summary, không gọi LLM lại

```python
# ai/summarizer.py
class ChapterSummarizer:
    def __init__(self, llm: LLMClient):
        self.llm = llm
    
    def summarize(self, story: Story, chapter_num: int, raw_text: str) -> str:
        # Cache check
        if chapter_num in story.chapter_summaries:
            return story.chapter_summaries[chapter_num]
        
        # Context: dùng tags + summary của 2-3 chap trước để AI hiểu context
        context = self._build_context(story, chapter_num)
        
        # Nếu text quá dài (> 8000 chars), chunk
        if len(raw_text) > 8000:
            return self._summarize_long(story, chapter_num, raw_text, context)
        
        prompt = f"""Tóm tắt chapter {chapter_num} của truyện "{story.title}":

CONTEXT (chapter trước):
{context}

NỘI DUNG CHAPTER:
{raw_text}

Tóm tắt 3-5 câu, tập trung vào: nhân vật chính làm gì, sự kiện quan trọng, plot twist (nếu có)."""
        
        summary = self.llm.generate(prompt)
        story.chapter_summaries[chapter_num] = summary
        return summary
```

##### 3.3 Recap Feature — "Đọc đến đâu rồi?"

User: "Tôi đọc đến chap 47 rồi nhưng đã 1 tuần không đọc, nhắc lại 5 chap gần nhất giúp"

```python
def recap(self, story: Story, n_chapters: int = 5) -> str:
    """Gộp summary của n chapter gần nhất thành 1 recap mạch lạc."""
    current = story.current_chapter
    summaries = [
        story.chapter_summaries[i]
        for i in range(max(1, current - n_chapters + 1), current + 1)
        if i in story.chapter_summaries
    ]
    if not summaries:
        return "Chưa có summary nào. Hãy summarize chapter trước."
    
    prompt = f"""Tổng hợp các đoạn tóm tắt chapter sau thành 1 recap liền mạch, dễ đọc:

{chr(10).join(f'Chap {i}: {s}' for i, s in enumerate(summaries, 1))}

Recap (5-7 câu):"""
    return self.llm.generate(prompt)
```

##### 3.4 Auto-Tag Suggester — Structured Output

User paste 1 đoạn description, AI suggest tags. **Quan trọng**: AI phải trả về JSON parseable.

```python
# ai/tagger.py
import json

AUTO_TAG_PROMPT = """Phân tích đoạn description truyện sau và đề xuất tag.
Chỉ trả về JSON đúng format, không có text khác.

Description: {description}

Tag pool có sẵn (chỉ chọn từ đây): {available_tags}

Format JSON:
{{
  "tags": ["tag1", "tag2", ...],
  "ending": "HE" | "BE" | "SE" | "OE" | null,
  "confidence": 0.0-1.0
}}"""

class AutoTagger:
    def __init__(self, llm: LLMClient, tag_trie: TagTrie):
        self.llm = llm
        self.tag_trie = tag_trie
    
    def suggest(self, description: str) -> dict:
        available = self.tag_trie.all_tags()    # tag pool đã có
        prompt = AUTO_TAG_PROMPT.format(
            description=description,
            available_tags=", ".join(available)
        )
        raw = self.llm.generate(prompt, json_mode=True)
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # AI không trả về JSON đúng → fallback
            return {"tags": [], "ending": None, "confidence": 0.0}
```

> 💡 **Insight:** Get LLM trả JSON đúng format là một cái art. Em sẽ phải iterate prompt 5-10 lần. Welcome to **prompt engineering**, một core skill của AI Engineer.

##### 3.5 Character Extractor (optional but cool)

Đọc qua các summary, extract nhân vật chính/phụ, lưu lại để xem bảng nhân vật:

```python
# Output mẫu:
👥 Nhân vật trong "Trọng Sinh Chi Đích Nữ":
   PROTAGONIST  Tô Lan      (đích nữ trọng sinh, thông minh)
   LOVE INTEREST Tần Mạc    (thái tử, lạnh lùng ngoài ấm trong)
   ANTAGONIST   Diệp Khả Tâm (giả vờ hiền lành, kiếp trước hại Tô Lan)
```

#### Definition of Done Phase 3:

- [ ] `summarize <story_id> <chapter>` paste text → AI tóm tắt → lưu lại
- [ ] `recap <story_id> [n]` tóm tắt n chap gần nhất thành recap mạch lạc
- [ ] `auto-tag <story_id>` AI đề xuất tag
- [ ] Streaming output khi summarize (in từng từ)
- [ ] Tắt Ollama → app không crash, in error message rõ ràng, gợi ý "chạy `ollama serve`"
- [ ] Mock `LLMClient` trong test → test logic summarizer mà không gọi API thật
- [ ] Cache summary: gọi summarize lần 2 cùng chapter → instant return, không gọi LLM

---

### 📅 Phase 4: Polish & Mini RAG (Tuần 4)

**Mục tiêu:** TUI đẹp, RAG để hỏi đáp về truyện đã đọc, export, README chuyên nghiệp.

#### Học được gì:
- Rich library cho TUI (Layout, Panel, Table, Live)
- **RAG basic**: embeddings + retrieval (chỉ entry-level, không cần vector DB)
- Export markdown (em có thể share recap với hội bạn)
- Logging
- README professional với screenshot/GIF
- Schema versioning (save game v1 đọc được khi đã update v2?)

#### Yêu cầu:

##### 4.1 Rich TUI

Layout chia 3 panel:
```
┌─────────────────────────┬───────────────────────┐
│  📚 Đang đọc            │  📊 Stats             │
│  ▸ Trọng Sinh...   47   │  Total: 47 truyện     │
│  ▸ Em Là Cô Gái... 12   │  Đọc 2025: 1.2M chữ   │
├─────────────────────────┤  Top tag: ngọt sủng   │
│  🎯 TBR Top 3           │                       │
│  1. Cô Vợ Nhỏ Của Boss  ├───────────────────────┤
│  2. Anh Trai Nuôi Em    │  💭 Hôm nay đọc gì?  │
└─────────────────────────┴───────────────────────┘
> _
```

##### 4.2 Mini RAG — Hỏi đáp truyện đã đọc

User: "Tô Lan có anh chị em ruột không?" → app retrieve những summary có chứa "Tô Lan" + family-related → feed vào LLM → answer.

**Đây là RAG bare-minimum**, không cần vector DB hay embedding model. Dùng inverted index Phase 2!

```python
# ai/rag.py
class StoryRAG:
    def __init__(self, llm: LLMClient, library: Library, index: InvertedIndex):
        self.llm = llm
        self.library = library
        self.index = index
    
    def ask(self, story_id: str, question: str) -> str:
        story = self.library.get(story_id)
        # Retrieve: tìm chapter summaries liên quan question
        question_words = self.index._tokenize(question)
        relevant_chapters = self._retrieve_chapters(story, question_words)
        
        if not relevant_chapters:
            return "Không tìm thấy thông tin liên quan trong truyện này."
        
        # Augment: build context
        context = "\n\n".join(
            f"Chap {ch}: {story.chapter_summaries[ch]}"
            for ch in relevant_chapters
        )
        
        # Generate
        prompt = f"""Dựa vào những đoạn tóm tắt sau từ truyện "{story.title}", trả lời câu hỏi.
Nếu không có thông tin, nói thẳng "Không có thông tin trong các chap đã đọc."

CONTEXT:
{context}

CÂU HỎI: {question}

TRẢ LỜI:"""
        return self.llm.generate(prompt)
```

> 🎓 **Insight quan trọng:** Cái em vừa build là kiến trúc RAG chuẩn — Retrieve, Augment, Generate. Production RAG dùng vector embeddings thay cho keyword matching, nhưng pattern y hệt. Em đã touch vào core skill của RAG Engineer rồi.

##### 4.3 Export to Markdown

Command `export <story_id>` → tạo file `exports/trong-sinh-chi-dich-nu.md` với toàn bộ thông tin + summary đẹp đẽ. Bạn ấy có thể paste lên Notion/blog share với hội cùng đọc.

##### 4.4 Statistics Dashboard

Command `stats` → in ra:
- Tổng số truyện theo status
- Top 5 tag em đọc nhiều nhất
- Reading streak (số ngày liên tiếp có cập nhật)
- Tổng số chữ đã đọc (estimate từ chapter count × avg chap length)
- Truyện chấm điểm cao nhất

#### Stretch goals (chỉ làm nếu còn thời gian):

- 🌐 **Web UI**: dùng FastAPI wrap thành web app
- 🔍 **Real RAG with embeddings**: dùng `sentence-transformers` + FAISS
- 📊 **Reading insights**: AI phân tích pattern đọc của em ("3 tháng qua bạn đọc 70% là tag XYZ, có vẻ bạn đang thích...")
- 🤝 **Friend mode**: import library của bạn, AI đề xuất truyện overlap
- 📱 **Mobile sync**: lưu lên Google Drive/Dropbox

---

## 🧠 Crash Course: OOP qua project này

| Principle | Em sẽ gặp ở đâu |
|---|---|
| **Encapsulation** | `Story.chapter_summaries` không expose trực tiếp — set qua method `add_summary()` để có validation |
| **Inheritance** | `LLMClient` abstract → `OllamaClient`, mai mốt `OpenAIClient` |
| **Polymorphism** | UI gọi `client.generate()` không quan tâm là Ollama hay Mock |
| **Composition** | `Library` HAS-A `dict[str, Story]`. `Story` HAS-A `dict[int, str]` cho summaries. `RAG` HAS-A `LLMClient` + `InvertedIndex` |

> ⚠️ **Pitfall:** Lạm dụng inheritance. Khi không chắc, dùng composition. "Favor composition over inheritance" — em sẽ ngộ ra qua chính code của mình.

---

## 🔥 Ollama + Tiếng Việt Crash Course

```bash
# Cài Ollama (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Pull qwen2.5 3B - tốt cho tiếng Việt
ollama pull qwen2.5:3b

# Test
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:3b",
  "prompt": "Tóm tắt: Một cô gái xuyên không về thời cổ đại...",
  "stream": false
}'
```

**Model recommendation:**

| RAM | Recommendation | Notes |
|---|---|---|
| 8GB | `qwen2.5:3b` | Tiếng Việt OK, tóm tắt tốt |
| 16GB | `qwen2.5:7b` | Tiếng Việt mượt hẳn, suggest mạnh |
| 32GB+ | `qwen2.5:14b` hoặc `qwen2.5:32b` | Gần GPT-3.5 quality |

**Tips quan trọng:**
- Prompt LUÔN viết tiếng Việt khi muốn output tiếng Việt
- Dùng `temperature=0.3` cho task summary (cần consistent), `0.7` cho creative
- Set `num_ctx=4096` nếu chapter dài
- Trường hợp model trả tiếng Anh ngẫu nhiên → thêm "Trả lời BẰNG TIẾNG VIỆT" vào cuối prompt

---

## ⚠️ Những lúc em sẽ muốn bỏ cuộc — và làm gì khi đó

Tôi nói thẳng: em sẽ stuck. Đây là moment phổ biến và cách qua:

1. **"Code lộn xộn quá, không biết để class này ở đâu"** → Dừng code, vẽ ra giấy hoặc Excalidraw quan hệ giữa class. 15 phút vẽ tiết kiệm 3 giờ refactor.

2. **"AI tóm tắt tệ quá, output dở/sai/dài quá"** → Vấn đề 90% là prompt. Test prompt trên `ollama run qwen2.5:3b` interactively trước khi đưa vào code. Iterate 5-10 lần. Đừng đổi model đầu tiên.

3. **"Em viết code chạy được nhưng nhìn xấu, không biết có đúng OOP không"** → Code chạy được = thành công. Refactor là next step. Đừng đợi perfect mới ship.

4. **"Em mất 2 ngày debug một bug"** → Stop. Đứng dậy. Đi bộ. Quay lại với fresh mind. Hoặc rubber-duck: giải thích bug cho ChatGPT/Claude.

5. **"Em thấy không học được gì, chỉ đang code thôi"** → Sau mỗi phase, viết file `LEARNED.md` ghi 3 điều mới học. Giúp em thấy progress.

6. **"Project khác trên GitHub xịn hơn nhiều"** → Em đang build từ DSA-only đến full RAG mini-system trong 4 tuần. Đó là progress đáng nể. So sánh với chính em 1 tháng trước, không so với senior 5 năm exp.

7. **"Em scroll Twitter/LinkedIn thấy ai cũng đang ship thứ điên rồ"** → Đó là **imposter syndrome**, nó hit ai cũng có. Feed em được lựa "highlight reel" của người khác. Em đang so sánh **process của mình** với **kết quả tốt nhất của họ**. Mute keyword 1 tuần. Tham gia community thực tế (xem mục Tài nguyên).

8. **"Trie/Inverted Index sao khó implement quá"** → Implement naive version trước (dùng list, dict thông thường). Cho chạy đúng đã. Sau đó refactor sang Trie. Đừng cố perfect lần đầu.

---

## ✅ Definition of Done — toàn project

Project được coi là DONE khi:

- [ ] App chạy được end-to-end: add story → tag → summarize → recap → ask RAG → export
- [ ] **20+ truyện** thật trong library (em đã/đang/muốn đọc)
- [ ] Trie autocomplete hoạt động trên 50+ tag
- [ ] Inverted index search hoạt động
- [ ] Similar stories đề xuất hợp lý (Jaccard)
- [ ] TBR ranking với mood filter
- [ ] AI summarize chapter chạy được (paste text → output)
- [ ] AI auto-tag với JSON output parse được
- [ ] Mini RAG trả lời được câu hỏi từ summary đã có
- [ ] **Test coverage ≥ 60%** cho `core/`
- [ ] README có demo GIF/screenshot, đẹp, professional
- [ ] Repo public trên GitHub với commit history sạch
- [ ] **Một blog post ngắn** (Notion/Medium/Spiderum/dev.to) viết lại quá trình — đây là CV thật của em

---

## 🎁 Daily Habits — đừng skip

- **Daily commit**: 30 phút cũng commit. Streak quan trọng hơn volume.
- **Cuối ngày**: 2 dòng vào `JOURNAL.md` — hôm nay làm gì, mai làm gì.
- **Cuối tuần**: demo 1 phút cho mentor hoặc bạn cùng đọc ngôn tình. Giải thích = học chắc.
- **Khi stuck > 1 giờ**: hỏi. Không có gì shame.
- **Đọc 1 chapter ngôn tình mỗi ngày** rồi paste vào app summarize. Em vừa relax vừa test app vừa tạo dataset.

---

## 📚 Tài nguyên (chỉ đọc khi cần, đừng overload)

**OOP:**
- *Python OOP Tutorial* — Real Python (chỉ phần Classes & Inheritance)
- *Composition over Inheritance* — Brandon Rhodes (video, 30 phút)

**DSA Apply:**
- *Trie implementation* — LeetCode Explore (free)
- *Inverted Index simple* — Lucene blog hoặc bất kỳ NLP intro book

**Software dev:**
- *Pro Git* — chương 1 & 2
- *Architecture Patterns with Python* — Bob Gregory (chương 1-3)

**LLM & Prompt:**
- Ollama docs (30 phút)
- *Prompt Engineering Guide* — promptingguide.ai
- *RAG from Scratch* — LangChain blog (đọc concept, KHÔNG dùng LangChain)

**Communities (peer support quan trọng không kém tài liệu):**
- **Vietnam Women in Tech** — group FB/Discord, nhiều senior nữ hỗ trợ junior
- **PyLadies Vietnam** — chapter Hà Nội & HCM có meetup định kỳ
- **Women Who Code** — chapter VN
- **Discord Ollama** — hỏi gì về local LLM nhanh nhất
- **r/learnpython** — friendly cho người mới

> 💡 **Một observation:** Nếu em là nữ duy nhất trong team intern hiện tại, peer ngoài workplace cực kỳ quan trọng — không phải replace, mà là supplement.

**KHÔNG đọc** lúc này: Design Patterns (Gang of Four), Clean Architecture, DDD. Để sau project mới đọc — em sẽ hiểu sâu hơn nhiều.

---

## 🚀 Lời cuối từ Tech Lead

Em không phải build cái gì hoàn hảo. Em đang **build kỹ năng**, và cách build kỹ năng tốt nhất là **ship thật**.

4 tuần sau, em sẽ có:
- Một app em DÙNG THẬT mỗi ngày
- Một GitHub repo có code chất lượng decent
- Hiểu OOP từ thực hành chứ không phải lý thuyết
- DSA của em đã apply vào bài thật, không còn là kiến thức "tôi đã học"
- Touch vào toàn pipeline: domain → DSA → AI → RAG → UI → persistence
- Câu chuyện kể được trong interview AI Engineer

Quan trọng nhất: em xây một thứ **PHỤC VỤ chính em**. Đó là động lực bền vững nhất trong nghề. Mỗi feature em add, là life em được nâng cấp.

Khi nào em muốn debate design, refactor, hay stuck — ping tôi. Cứ ship trước, perfect sau.

Now go cook. 🌸🔥

— *Tech Lead*

---

## 📋 Quick Checklist (in ra dán lên màn hình)

```
PHASE 0 [ ] Setup + Hello Ollama tiếng Việt
PHASE 1 [ ] Library CRUD + tags (no LLM, đã dùng được)
PHASE 2 [ ] Trie + Inverted Index + Graph + PriorityQueue
PHASE 3 [ ] AI Summarize + Auto-tag + Recap
PHASE 4 [ ] Mini RAG + TUI + README đẹp
```
