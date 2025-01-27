from app import create_app
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


try:
    from app import scheduler

    def test_project_structure():
        # Create the Flask app
        app = create_app()
        print("✅ Successfully created app")

        with app.app_context():
            # Test application context
            print("✅ App context is active")

            # Test scheduler
            if hasattr(scheduler, "running"):
                print(f"Scheduler running: {scheduler.running}")
            else:
                print("❌ Scheduler does not have a 'running' property")

            # Start the scheduler if not already running
            if hasattr(scheduler, "start") and not scheduler.running:
                print("Starting scheduler...")
                scheduler.start()

            # Clean up scheduler
            if scheduler.running:
                print("Shutting down scheduler...")
                scheduler.shutdown()

    if __name__ == "__main__":
        test_project_structure()

except ImportError as e:
    print(f"❌ Import Error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
