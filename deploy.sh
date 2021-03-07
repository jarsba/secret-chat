#!/bin/bash
rm -r build/*
pushd ../secret-chat-ui
npm run build
cp -ar build/. ../secret-chat/build/
popd
git push
git push heroku main
