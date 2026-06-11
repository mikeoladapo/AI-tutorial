import voyageai
import os
from dotenv import load_dotenv

vo = voyageai.Client()
document = "how are you doing today?"
result = vo.embed([document], model="voyage-4", input_type="document")
print(result.embeddings[0])