# Maintainer: Darion Kellar <credkellar@gmail.com>

pkgname=sandb0x-xtractor-git
pkgver=0.2.0.r0.g1234567
pkgrel=1
pkgdesc="Automated cross-platform security analysis engine using multi-LLMs"
arch=('any')
url="https://github.com/darnellwashingtonjr94-art/Sandb0x-Xtract0r"
license=('MIT')
depends=('python' 'python-pip')
makedepends=('git')
groups=('blackarch' 'blackarch-webapp' 'blackarch-malware')
source=("git+https://github.com/darnellwashingtonjr94-art/Sandb0x-Xtract0r.git")
sha512sums=('SKIP')

pkgver() {
  cd "Sandb0x-Xtract0r"
  (
    set -o pipefail
    git describe --long --tags --abbrev=7 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
      printf "%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  )
}

package() {
  cd "Sandb0x-Xtract0r"
  
  # Create destination directories
  install -dm755 "$pkgdir/usr/share/$pkgname"
  install -dm755 "$pkgdir/usr/bin"

  # Copy project files into share directory
  cp -r . "$pkgdir/usr/share/$pkgname/"

  # Create a wrapper script to execute main.py cleanly
  cat << EOF > "$pkgdir/usr/bin/sandb0x-xtractor"
#!/bin/bash
cd /usr/share/$pkgname
exec python3 main.py "\$@"
EOF

  chmod +x "$pkgdir/usr/bin/sandb0x-xtractor"
}
