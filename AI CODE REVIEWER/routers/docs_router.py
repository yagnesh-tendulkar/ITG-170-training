# ─────────────────────────────────────────────
# routers/docs_router.py
#
# Documentation generation endpoint
# ─────────────────────────────────────────────

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas
from auth import get_current_user
from services.ai_service import generate_documentation

router = APIRouter(prefix="/docs-gen", tags=["Documentation"])


@router.post("/generate", response_model=schemas.DocsResponse)
async def generate_docs(
    request: schemas.DocsRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Generate documentation for a given code snippet.
    Supports Google-style, NumPy-style (Python), and JSDoc (JavaScript).
    """
    result = await generate_documentation(
        language=request.language,
        code=request.code,
        doc_style=request.doc_style,
    )

    return schemas.DocsResponse(
        original_code=request.code,
        documented_code=result.get("documented_code", request.code),
        explanation=result.get("explanation", ""),
    )
