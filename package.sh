#!/usr/bin/env bash

# remove old package
rm -rf package.tar.gz

# build app
npm run build

# gather things
mkdir package
cp -r public/* package/

tar -czf package.tar.gz -C package .
rm -rf package
