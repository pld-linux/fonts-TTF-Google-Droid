#!/bin/sh
#Try to get upstream latest files (from fc)

DATE=$(date -u +%Y%m%d)
ARCHIVE="google-droid-fonts-$DATE"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp getdroid-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
olddir=$(pwd)
cd "$TMPDIR" || exit 1
git init
git remote add -t HEAD origin https://android.googlesource.com/platform/frameworks/base.git
git config core.sparseCheckout true
cat > .git/info/sparse-checkout << 'EOF'
data/fonts/*
!data/fonts/*ttf
data/fonts/Droid*
EOF
git pull --no-tags origin HEAD
LDATE=$(git log --first-parent --format='%ci' -n 1 master data/fonts)
DATE=$(date "+%Y%m%d" -d ${LDATE%% *})
ARCHIVE="google-droid-fonts-$DATE"
git log data/fonts > ChangeLog
mv data/fonts "$ARCHIVE"
mv ChangeLog "$ARCHIVE/ChangeLog"
chmod -x $ARCHIVE/*.ttf
tar -cvJf "$ARCHIVE.tar.xz" "$ARCHIVE"
cd "$olddir"
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
