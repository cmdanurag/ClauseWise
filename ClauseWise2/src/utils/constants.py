class SupportedFileTypes:
    PDF = "application/pdf"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    TXT = "text/plain"
    
    @classmethod
    def get_all(cls):
        return [cls.PDF, cls.DOCX, cls.TXT]


class LegalDocumentTypes:
    RENTAL_AGREEMENT = "rental_agreement"
    LOAN_CONTRACT = "loan_contract"
    TERMS_OF_SERVICE = "terms_of_service"
    EMPLOYMENT_CONTRACT = "employment_contract"
    GENERAL_CONTRACT = "general_contract"


class RiskLevels:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# ✅ File validation constants (must be top-level, not inside a class)
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = [".pdf", ".docx", ".txt"]
