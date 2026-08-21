class SandboxXtractor < Formula
  # ... (desc, homepage, url, sha256)

  depends_on "python@3.12"

  # Generated resources go here:
  resource "requests" do
    url "https://files.pythonhosted.org/packages/..."
    sha256 "..."
  end

  def install
    # ...
  end
end
