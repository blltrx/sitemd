{ pkgs }:
pkgs.mkShell {
  name = "python-htmldown";
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      # python-pkgs.pandas
      # python-pkgs.requests
      python-pkgs.markdown
    ]))
  ];
  shellHook = "./build.sh && git push";
}
