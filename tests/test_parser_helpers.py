from spirit.parsers.parser_helpers import run_parser


def test_run_parser():
    packet = b'\n\xdf\x01\n$344292aa-c441-4fc0-82dc-572f2da78047\x10\xd8\xc6\xcf\xff\xec-\x1aC\n\x1b\t\x00\x00\x00`\xda\xb1\xe5\xbf\x11\x00\x00\x00\xe0\x9b\x10\x9c?\x19\x00\x00\x00 Fa\x0f@\x12$\tpc\xbd\xf7\x8f\x04\xbf\xbf\x11\xd5\xfb?y\xdcX\xc9?\x1965\xa0\x1a:.\xa4?!\xfd\xc5\xb7\xb7\xa5\x19\xef?",\x08\x80\x0f\x10\xb8\x08\x1a$242d1971-ea71-4b6e-a508-59216e0425c5*,\x08\xac\x01\x10\xe0\x01\x1a$3289b81e-466e-44e9-a48b-21dafbb115ed2\x0f\r\xb8\x1e\x05>\x15?5\xde\xbe\x1dj\xbct>\x12\x14\x08*\x12\nDan Gittik\x18\xe0\x90\xd5\xcd\x02'
    result = run_parser('pose', packet)
    assert result.rotation == (-0.12116336630186963, 0.19802432938010264,
                               0.03941518378278845, 0.9718807781447932)
    assert result.translation == (-0.6779605746269226, 0.02740710787475109, 3.922497034072876)