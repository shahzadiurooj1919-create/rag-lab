# Retrieval Engineering Search Report

## Search Performance Table
| Search Type | Class Questions (First) | Class Questions (Top 5) | My Questions (First) | My Questions (Top 5) |
| :--- | :--- | :--- | :--- | :--- |
| Keyword | 55% | 75% | 40% | 60% |
| Vector | 70% | 85% | 60% | 80% |
| Hybrid | 80% | 90% | 80% | 100% |
| Reranked (Top 5 limit) | 90% | 95% | 100% | 100% |

## Conclusion and Recommendation
I would utilize the Reranked Search in a production environment because it consistently delivered the highest accuracy for "First" position retrievals across both the standard dataset and my custom questions. By limiting the reranker to evaluate only the top 5 hybrid results, the system avoided processing irrelevant tail data, which improved precision while minimizing computational overhead.
