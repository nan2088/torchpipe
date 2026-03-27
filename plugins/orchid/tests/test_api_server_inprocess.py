from fastapi.testclient import TestClient

from orchid.llmscheduler.server.config import ServerConfig
from orchid.llmscheduler.server.app_factory import create_app


def test_chat_completions_test_mode():
    config = ServerConfig(
        host="127.0.0.1",
        port=0,
        test_mode=True,
        model_path="",
        tokenizer_path="",
        use_fp16=True,
        engine_path=None,
        num_layers=None,
        num_heads=None,
        kv_num_heads=None,
        head_dim=None,
        page_size=16,
        max_pages=None,
    )
    app = create_app(config)
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["ready"] is True

    body = {"model": "x", "messages": [{"role": "user", "content": "hi"}], "stream": False, "max_tokens": 4}
    r = client.post("/v1/chat/completions", json=body)
    assert r.status_code == 200
    j = r.json()
    assert j["choices"][0]["message"]["content"] == "ok"

