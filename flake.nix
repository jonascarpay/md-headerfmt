{
  description = "md-headerfmt";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/release-22.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = inputs:
    let
      overlay = final: prev: {
        md-headerfmt = final.stdenv.mkDerivation {
          pname = "md-headerfmt";
          version = "1.0";
          buildInputs = [ final.python3 ];
          unpackPhase = "true";
          installPhase = ''
            mkdir -p $out/bin
            cp ${./md-headerfmt.py} $out/bin/md-headerfmt
          '';
        };
      };
      perSystem = system:
        let
          pkgs = import inputs.nixpkgs {
            inherit system;
            overlays = [ overlay ];
          };
        in
        {
          devShell = pkgs.mkShell {
            packages = [
              pkgs.python3
              pkgs.black
              pkgs.pyright
            ];
          };
          defaultPackage = pkgs.md-headerfmt;
          packages.md-headerfmt = pkgs.md-headerfmt;
        };
    in
    { inherit overlay; } // inputs.flake-utils.lib.eachDefaultSystem perSystem;
}
