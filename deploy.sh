#!/bin/bash
rm -r build/*
pushd ../secret-chat-ui
npm run build
cp -ar build/. ../secret-chat/build/
popd
git add *
git commit -m "Deploy to Heroku"
git push
git push heroku main
heroku logs --tail
