import asyncio
import cognee
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Reset memory (clean slate)
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    print("Step 1: Storing incident into memory...")

    # This is a fake incident report we're feeding to ThreatDNA
    incident = """
    Incident Report #001 - Date: 2026-01-15
    Severity: Critical
    
    A PowerShell script was detected running encoded commands on WORKSTATION-42.
    The script downloaded a payload from a remote server.
    The malware was identified as Emotet.
    MITRE ATT&CK techniques: T1059 (PowerShell), T1055 (Process Injection).
    CVE exploited: CVE-2026-1234.
    Affected systems: WORKSTATION-42, SERVER-FINANCE-01.
    Analyst note: Attackers gained persistence within 12 minutes. LSASS was dumped.
    """

    await cognee.remember(incident)

    print("Step 2: Memory stored! Now asking a question...")

    results = await cognee.recall("PowerShell malware attack techniques")

    print("\n--- ThreatDNA Answer ---")
    for result in results:
        print(result)

asyncio.run(main())