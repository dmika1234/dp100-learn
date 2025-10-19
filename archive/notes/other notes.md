**Finding creation and update details of a resource**
1. Go to  Azure Resource Graph Explorer.
2. Run this query:
    ```
    resourcechanges
    | where resourceGroup == "rgname"
    | extend changeTime = todatetime(properties.changeAttributes.timestamp), targetResourceId = tostring(properties.targetResourceId),
    changeType = tostring(properties.changeType), correlationId = properties.changeAttributes.correlationId
    |where changeType == "Create" or changeType == "Update"
    | order by changeTime desc
    | project changeTime, resourceGroup, targetResourceId, changeType, correlationId
    ```