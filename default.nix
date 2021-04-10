with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "wallabag-cli";
  buildInputs = [
    (pkgs.python36.withPackages (pythonPackages: with pythonPackages; [
      beautifulsoup4
      pycrypto
      requests
    ]))
  ];
  unpackPhase = "true";
  installPhase = ''
    mkdir -p $out/bin
    cp -r ${./wallabag} $out/bin/wallabag_code
    ln -s $out/bin/wallabag_code/wallabag.py $out/bin/wallabag
    chmod +x $out/bin/wallabag
  '';
}

