import openai
import time
import logging

def interact_with_assistant(api_key, model, assistant_id, thread_id, user_message):
    # Initialize OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    # Create a message in the thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=user_message
    )

    # Create a run for the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    
    def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
        while True:
            try:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
                if run.completed_at:
                    elapsed_time = run.completed_at - run.created_at
                    formatted_elapsed_time = time.strftime(
                        "%H:%M:%S", time.gmtime(elapsed_time)
                    )
                    logging.info(f"Run completed in {formatted_elapsed_time}")
                    # Get messages here once Run is completed!
                    messages = client.beta.threads.messages.list(thread_id=thread_id)
                    last_message = messages.data[0]
                    response = last_message.content[0].text.value
                    return response
            except Exception as e:
                logging.error(f"An error occurred while retrieving the run: {e}")
                break
            logging.info("Waiting for run to complete...")
            time.sleep(sleep_interval)

    # Wait for the run to complete and get the response
    response = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)
    return response

