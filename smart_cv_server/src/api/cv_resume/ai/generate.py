class CVGenAI:
    def generate_cv_body(self, cv_resume):
        # Accessing related objects through the ManyToMany fields
        skill_list = ", ".join([skill.name for skill in cv_resume.skills.all()])
        language_list = ", ".join([language.name for language in cv_resume.personal_info.languages.all()])
        certification_name = cv_resume.certification.name if cv_resume.certification else ""
        # Define the body content using placeholders for dynamic values
        body_content = f"""
        <p>I am a dedicated and driven professional. 
        Throughout my education at {cv_resume.education.institute}, I developed a solid foundation in 
        {cv_resume.education.field_of_study}, which has been further strengthened by my hands-on experience 
        at {cv_resume.workExperience.company}.</p>

        <p>My role as {cv_resume.workExperience.position} involved responsibilities such as 
        {cv_resume.workExperience.responsibilities}. This experience has equipped me with essential skills 
        like {skill_list}, making me proficient in various aspects of the field.</p>

        <p>I am fluent in {language_list}, which allows me to communicate effectively in diverse environments. 
        My strong analytical and problem-solving skills, coupled with my ability to adapt to new challenges, 
        make me an asset to any team.</p>

        <p>I am committed to continuous learning and professional development, evidenced by my certifications 
        in {certification_name}. I am excited about the opportunity to contribute to a dynamic organization.</p>
        """
        return body_content
