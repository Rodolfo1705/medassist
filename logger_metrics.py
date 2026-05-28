import datetime
import pandas as pd
import os


class SecurityLogger:
    LOG_FILE = "security_logs.csv"

    @staticmethod
    def log_event(event_type: str, detail: str, status: str, ai_response: str = ""):
        new_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": event_type,
            "detail": detail,
            "status": status,
            "ai_response": ai_response
        }

        df = pd.DataFrame([new_entry])

        if not os.path.isfile(SecurityLogger.LOG_FILE):
            df.to_csv(SecurityLogger.LOG_FILE, index=False)
        else:
            try:
                # Tenta ler apenas o cabeçalho para verificar as colunas
                existing_cols = pd.read_csv(
                    SecurityLogger.LOG_FILE, nrows=0).columns.tolist()
                if "ai_response" not in existing_cols:
                    # Se não existir, lê o arquivo todo e adiciona a coluna
                    full_df = pd.read_csv(SecurityLogger.LOG_FILE)
                    full_df["ai_response"] = ""
                    full_df = pd.concat([full_df, df], ignore_index=True)
                    full_df.to_csv(SecurityLogger.LOG_FILE, index=False)
                else:
                    # Se já existir, apenas anexa
                    df.to_csv(SecurityLogger.LOG_FILE, mode='a',
                              header=False, index=False)
            except Exception:
                # Em caso de erro catastrófico no CSV, cria um novo
                df.to_csv(SecurityLogger.LOG_FILE, index=False)

    @staticmethod
    def get_logs():
        if os.path.isfile(SecurityLogger.LOG_FILE):
            return pd.read_csv(SecurityLogger.LOG_FILE)
        return pd.DataFrame(columns=["timestamp", "event_type", "detail", "status", "ai_response"])

    @staticmethod
    def get_metrics():
        logs = SecurityLogger.get_logs()
        if logs.empty:
            return {"Bloqueios": 0, "Aprovações HITL": 0, "Total": 0}

        metrics = {
            "Bloqueios": len(logs[logs['status'] == "blocked"]),
            "Aprovações HITL": len(logs[logs['status'] == "hitl_approved"]),
            "Total": len(logs)
        }
        return metrics
