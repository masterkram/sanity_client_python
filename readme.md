# Sanity Python Client

Python client that is able to send `groq` queries to a [sanity](https://sanity.io) dataset and get the results as json.

```python
sanity_client = SanityClient(
  project_id="example_id",
  dataset="production"
)

sanity_client.fetch("*[_type=='yupipack']{'id': _id, name, image, description} | order(order desc)")
```