#!/bin/bash

# Get the latest tag from GitHub
LATEST_TAG=$(curl -s https://api.github.com/repos/nadzzdan/3tierapp/tags | jq -r '.[0].name')

if [ "$LATEST_TAG" = "null" ] || [ -z "$LATEST_TAG" ]; then
    echo "No tags found, using latest"
    LATEST_TAG="latest"
fi

echo "Latest tag: $LATEST_TAG"

# Update kustomization.yaml
cd k8s/overlays/production
sed -i "s/newTag: latest/newTag: $LATEST_TAG/g" kustomization.yaml
sed -i "s/newTag: v[0-9]*\.[0-9]*\.[0-9]*/newTag: $LATEST_TAG/g" kustomization.yaml

echo "Updated kustomization.yaml with tag: $LATEST_TAG"

# Show the changes
echo "Current kustomization.yaml content:"
cat kustomization.yaml
