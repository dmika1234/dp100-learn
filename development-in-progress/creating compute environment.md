### Building environment images

If you need to build custom environment images, an appropriately provisioned Azure Container Registry (ACR) may be required (SKU and permissions depend on the scenario). Example Python snippet showing how to set the image build compute on a workspace object and update it via the MLClient:

```python
# ws is your workspace object
ws.image_build_compute = "your-cluster"
ml_client.workspaces.begin_update(ws)
```
Notes:
- Some image build scenarios require a Premium ACR SKU or specific permissions.
- Ensure networking and role assignments allow the workspace to push/pull images to/from ACR.