# ShippingTracker MCP Server

한국 택배 배송 조회를 위한 MCP (Model Context Protocol) 서버입니다. SweetTracker API를 사용하여 택배사 목록과 운송장 번호를 조회합니다.

## 기능

- `get_company_list()`: 지원하는 택배회사 목록 조회
- `track_shipping(company_code, tracking_invoice)`: 배송 조회
  
## 사전 요구사항

- [SweetTracker (스마트택배)](https://www.sweettracker.co.kr/) API 키

## 로컬 개발

### 1. 저장소 클론

```bash
git clone https://github.com/gws8820/shipping-tracker.git
cd shipping-tracker
```

### 2. 환경변수 설정

```bash
echo "SWEETTRACKER_API_KEY=YOUR_API_KEY" > .env
```

### 3. 실행

```bash
uv run python -m shipping-tracker.main

# 또는 uvx로 실행
uvx --from . shipping-tracker
```

## Claude Desktop과 연결

Claude Desktop의 설정 파일(`claude_desktop_config.json`)을 다음과 같이 설정해 주세요.

```json
{
  "mcpServers": {
    "shipping-tracker": {
      "command": "uvx",
      "args": ["shipping-tracker"],
      "env": {
        "SWEETTRACKER_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)하에 배포됩니다.
