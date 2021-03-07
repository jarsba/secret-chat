#!/bin/bash
pushd ../secret-chat-ui
npm run build
cp -r build/ ../secret-chat/build
popd
