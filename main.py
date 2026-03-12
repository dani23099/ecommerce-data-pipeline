import subprocess
import sys


def run_step(script_name, step_description):
    print(f"\n{'=' * 60}")
    print(f"⏳ STEP: {step_description} ({script_name})")
    print(f"{'=' * 60}")

    try:
        # sys.executable ensures it uses your exact Python environment
        subprocess.run([sys.executable, script_name], check=True)
        print(f"✅ SUCCESS: {script_name} completed without errors.")
    except subprocess.CalledProcessError:
        print(f"\n❌ CRITICAL ERROR: {script_name} failed.")
        print("🚨 Halting the entire pipeline to prevent data corruption.")
        sys.exit(1)  # Stops the program completely


if __name__ == "__main__":
    print("\n🌟 INITIATING MASTER DATA PIPELINE 🌟")

    # The order of execution is strictly sequential (ETL)
    run_step("extract.py", "Extracting raw data from API")
    run_step("analyze.py", "Applying Business Intelligence logic")
    run_step("visualize.py", "Generating strategic charts")
    run_step("load.py", "Loading data securely into MariaDB")

    print("\n🎉 ALL SYSTEMS GO: Master pipeline executed successfully! \n")