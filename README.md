# queryclassifier
Search queries can be simple or can be more human like so sometimes it is worth to pass them by a semantic search engine. This repo helps to build a simple classifier for Knowledge Mining solutions, we are show casing two options:
  A) NLP classification with Open AI Davinci engine: We will train the model with 10-15 different queries and provide labelling for GPT-3 to train a model on the go (other options are possible with a pretrained, deployed model)
  B) Simple javascript logic to count number of query terms, less accurate than A but way faster and more cost efficient 
both options include a language detector in case the query is classified as Semantic, the detection is based on Azure Cognitive Services Language service.

The reason to over simplify in B) and just count the number of terms in the query is because Semantic Search tends to work better when a context is given or when a question is phrased in a human like writting. Query terms like "A-13535 2005" are more token/syntax targeted to be matched against our inverted index solely through BM-25 algorithms while other queries like "How many weeks of paternity leave do I get while working for Microsoft Dubai?" have an extra degree of complexity, include context and would improve relevancy with the Semantic Reranker (https://docs.microsoft.com/en-us/azure/search/semantic-ranking) and would definitely leverage from Semantic Answers functionality (https://docs.microsoft.com/en-us/azure/search/semantic-answers?tabs=semanticConfiguration).

Production deployments will probably demand the accuracy of A) with the simplicity of B) to achieve a low latency and highly effective service.
