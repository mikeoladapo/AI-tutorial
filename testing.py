import voyageai
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

voyageai.api_key = os.getenv("VOYAGE_API_KEY")


vo = voyageai.Client()
document = ["I'm doing well today","She is fine","we are all good"]
doc_embed = vo.embed(document, model="voyage-4", input_type="document").embeddings
query = "how are you doing today?"
query_embed = vo.embed([query],model="voyage-4", input_type="query").embeddings[0]
similarities = np.dot(doc_embed,query_embed)
result_id = np.argmax(similarities)
print(document[result_id])