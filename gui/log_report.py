import logging

class ReportLog():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Set the logging level

        # Create a file handler and formatter
        file_handler = logging.FileHandler('app.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler) 


        try:
            self.logger.info('Reporting!')
        except Exception as e:
            self.logger.error(f"Error: {e}")

# import logging

# class ReportLog():
#     def __init__(self):
#         try:
#             print('Reporting!')
#         except Exception as e:
#             print(f"Error {e}")