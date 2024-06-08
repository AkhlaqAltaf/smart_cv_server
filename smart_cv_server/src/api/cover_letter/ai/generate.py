class CoverLetterGenAI:
    def generate_cover_letter_body(self, cover_letter):
        job_title = cover_letter.job_title
        company_name = cover_letter.company_name
        job_description = cover_letter.job_description
        name = cover_letter.name
        phone_number = cover_letter.phone_number
        email = cover_letter.email
        address = cover_letter.address
        experience = cover_letter.experience

        # Define the body content using placeholders for dynamic values
        body_content = f"""
       

        I am writing to express my interest in the {job_title} position at {company_name}, as advertised [where you found the job posting]. 
        With a strong background in [mention relevant skills or experiences], I am confident in my ability to contribute effectively to your team.

     In my previous role at [previous company], I [mention relevant achievements or experiences]. 
        These experiences have equipped me with [mention relevant skills or qualities] which I believe will be valuable in the {job_title} position.

     I am particularly excited about the opportunity to [mention something specific about the company or role that excites you]. 
        I am eager to bring my [mention relevant skills or experiences] to {company_name} and contribute to [mention what you hope to achieve in the role].

      Thank you for considering my application. I am looking forward to the opportunity to discuss how my background, skills, and enthusiasms align with the needs of {company_name}.

        """
        return body_content
