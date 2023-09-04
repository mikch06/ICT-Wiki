#!/bin/bash
# deploy generated html files to web
set -x

prod_dir='../www/kissel.ch/wein'
test_dir='web'

test() {
  if [ ! -d $test_dir ];
  then
  mkdir -p $test_dir
  fi

  echo "Deployment to test."
  rm -rf $test_dir/posts
  cp -r output/* $test_dir
}

prod() {
  if [ ! -d prod_dir ];
  then
  mkdir -p prod_dir
  fi

  echo "PRODUCTION Deployment."
  rm -rf prod_dir/posts
  cp -r output/* prod_dir
}}

case "$1" in
        test)
                test
                ;;
        prod)
                prod
                ;;

        *)
                echo "Please use option $0 {test|prod}"
esac