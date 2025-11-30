import datetime

def generate_email(candidate_name, decision, reasoning):
    """
    Acts as the Communication Agent. Generates a professional email 
    based on the final verified decision.
    
    Args:
        candidate_name (str): The name of the applicant.
        decision (str): "Interview" or "Reject".
        reasoning (str): The feedback summary to include (optional).
    """
    today_date = datetime.date.today().strftime("%B %d, %Y")
    
    if decision == "Interview":
        subject = f"Invitation to Interview - {candidate_name}"
        body = f"""
        Date: {today_date}
        To: {candidate_name}
        Subject: {subject}
        
        Dear {candidate_name},
        
        We are pleased to inform you that your application has been selected for the next round of interviews! 
        
        Our AI review team was particularly impressed by:
        {reasoning}
        
        Our scheduling coordinator will be in touch shortly to arrange a time.
        
        Best regards,
        Talent Acquisition Team
        """
        
    else:  # Rejection
        subject = f"Update on your application - {candidate_name}"
        body = f"""
        Date: {today_date}
        To: {candidate_name}
        Subject: {subject}
        
        Dear {candidate_name},
        
        Thank you for your interest in joining our team. 
        
        We have reviewed your application, and unfortunately, we have decided to proceed with other candidates who more closely match our specific requirements for this role at this time.
        
        Specific Feedback: {reasoning}
        
        We wish you the best in your job search.
        
        Sincerely,
        Talent Acquisition Team
        """
        
    return body