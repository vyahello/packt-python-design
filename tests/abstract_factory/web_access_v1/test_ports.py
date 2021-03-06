from patterns.factory.abstract_factory.web_access_v1.ports import HttpPort, HttpSecurePort, FTPPort

_http = '80'
_https = '443'
_ftp = '21'


def test_http_port():
    assert str(HttpPort()) == _http


def test_https_port():
    assert str(HttpSecurePort()) == _https


def test_ftp_port():
    assert str(FTPPort()) == _ftp
