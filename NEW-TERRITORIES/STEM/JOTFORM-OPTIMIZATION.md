# JotForm Optimization Guide for NT STEM Booking System

## Overview
This guide outlines the essential fields, logic, and optimizations needed for your JotForm booking form to effectively capture student enrollments and manage class registrations.

---

## 📋 Essential Form Fields

### Section 1: Parent/Guardian Information
- **Full Name** (Required, Text)
- **Email Address** (Required, Email)
- **Phone Number** (Required, Phone)
- **WhatsApp Number** (Optional, Phone) - For quick communication
- **Preferred Contact Method** (Required, Dropdown: Email / WhatsApp / Phone)

### Section 2: Student Information
- **Student Full Name** (Required, Text)
- **Student Date of Birth** (Required, Date) - Auto-calculates age
- **Student Age** (Auto-calculated from DOB, Display Only)
- **Gender** (Optional, Dropdown: Male / Female / Prefer not to say)

### Section 3: Program Selection
- **Program Type** (Required, Dropdown)
  - Regular Weekly Classes
  - Holiday Camp
  - Private Classes
  - Birthday Party
  - School Workshop
  - Other (please specify)

### Section 4: Class Details (Conditional - shows if "Regular Weekly Classes" selected)
- **Preferred Time Slot** (Required, Dropdown)
  - 4:00 PM - 5:00 PM (Beginners/Intermediate)
  - 5:00 PM - 6:00 PM (Intermediate/Advanced)
  - 6:00 PM - 7:00 PM (Advanced)
  - Flexible/Multiple slots

- **Student Level** (Required, Dropdown)
  - Beginner (First time STEM)
  - Intermediate (Some experience)
  - Advanced (Experienced)

- **Days per Week** (Required, Dropdown)
  - 1 day per week
  - 2 days per week
  - 3 days per week
  - 4 days per week
  - 5 days per week (Full week)

- **Start Date** (Required, Date)

- **Preferred Location** (Required, Dropdown)
  - Location 1 (Address)
  - Location 2 (Address)
  - Location 3 (Address)
  - Flexible/TBD

### Section 5: Special Programs (Conditional - shows if Holiday Camp/Birthday/Workshop selected)
- **Event Date** (Required, Date)
- **Number of Students** (Required, Number) - Minimum 3
- **Preferred Duration** (Required, Dropdown)
  - Half Day (4 hours)
  - Full Day (8 hours)
  - Custom (please specify)
- **Special Requests/Theme** (Optional, Long Text)

### Section 6: Health & Safety
- **Any Allergies?** (Optional, Text)
- **Medical Conditions** (Optional, Text)
- **Emergency Contact Name** (Required, Text)
- **Emergency Contact Phone** (Required, Phone)
- **Health Declaration** (Required, Checkbox)
  - "I confirm my child is in good health and able to participate in physical activities"

### Section 7: Additional Information
- **How did you hear about us?** (Optional, Dropdown)
  - Google Search
  - Social Media
  - Friend/Family Referral
  - School Recommendation
  - Other

- **What interests your child most?** (Optional, Checkboxes)
  - Architecture & Building
  - Robotics & Engineering
  - Space & Exploration
  - Environmental Science
  - Technology & Coding
  - Art & Design
  - Other

- **Additional Comments** (Optional, Long Text)

### Section 8: Pricing & Confirmation
- **Estimated Cost** (Display Only, Auto-calculated)
  - Regular Classes: HK$400/hour × days per week × 4 weeks
  - Holiday Camp: Custom quote
  - Private Classes: Custom quote
  - Birthday Party: From HK$2,000

- **Terms & Conditions** (Required, Checkbox)
  - "I agree to the cancellation policy and terms of service"

- **Marketing Consent** (Optional, Checkbox)
  - "I'd like to receive updates about new programs and special offers"

---

## 🔧 Conditional Logic Rules

### Rule 1: Show Class Details if Regular Classes Selected
```
IF Program Type = "Regular Weekly Classes"
THEN Show: Preferred Time Slot, Student Level, Days per Week, Start Date, Preferred Location
```

### Rule 2: Show Special Program Details if Holiday/Birthday/Workshop Selected
```
IF Program Type = "Holiday Camp" OR "Birthday Party" OR "School Workshop"
THEN Show: Event Date, Number of Students, Preferred Duration, Special Requests
```

### Rule 3: Auto-Calculate Age from DOB
```
Student Age = Current Year - Birth Year
(Use JotForm's built-in date calculation)
```

### Rule 4: Auto-Calculate Estimated Cost
```
IF Program Type = "Regular Weekly Classes"
THEN Estimated Cost = 400 × Days per Week × 4
ELSE IF Program Type = "Holiday Camp"
THEN Estimated Cost = "Custom Quote - Will contact you"
ELSE IF Program Type = "Private Classes"
THEN Estimated Cost = "Custom Quote - Will contact you"
ELSE IF Program Type = "Birthday Party"
THEN Estimated Cost = "From HK$2,000 - Will contact you"
```

### Rule 5: Require Emergency Contact if Student Under 18
```
IF Student Age < 18
THEN Make Emergency Contact Name & Phone Required
```

---

## 📧 Email Notifications

### Confirmation Email to Parent
**Trigger**: Form Submission
**Recipient**: Parent Email Address
**Subject**: "Your NT STEM Class Booking - Confirmation & Next Steps"

**Email Template Content**:
```
Dear [Parent Name],

Thank you for booking with New Territories STEM!

BOOKING DETAILS:
- Student: [Student Name]
- Program: [Program Type]
- Time Slot: [Time Slot] (if applicable)
- Start Date: [Start Date]
- Estimated Cost: [Estimated Cost]

NEXT STEPS:
1. We will contact you within 24 hours to confirm availability
2. Payment details will be sent via email
3. Class materials and location details will be provided 1 week before start

CONTACT US:
- Email: contact@ntstem.hk
- WhatsApp: +852 1234 5678
- Phone: +852 1234 5678

Questions? Reply to this email or contact us directly.

Best regards,
New Territories STEM Team
```

### Internal Notification to Admin
**Trigger**: Form Submission
**Recipient**: contact@ntstem.hk
**Subject**: "New Booking: [Student Name] - [Program Type]"

**Email Template Content**:
```
NEW BOOKING RECEIVED

PARENT INFORMATION:
- Name: [Parent Name]
- Email: [Email]
- Phone: [Phone]
- Preferred Contact: [Preferred Contact Method]

STUDENT INFORMATION:
- Name: [Student Name]
- Age: [Age]
- Level: [Level]

PROGRAM DETAILS:
- Type: [Program Type]
- Time Slot: [Time Slot]
- Days per Week: [Days]
- Location: [Location]
- Start Date: [Start Date]
- Estimated Cost: [Estimated Cost]

HEALTH INFORMATION:
- Allergies: [Allergies]
- Medical Conditions: [Medical Conditions]
- Emergency Contact: [Emergency Contact Name] - [Phone]

ADDITIONAL INFO:
- How they found us: [Source]
- Interests: [Interests]
- Comments: [Comments]

ACTION REQUIRED:
[ ] Confirm availability
[ ] Send payment details
[ ] Assign tutor
[ ] Send welcome package
```

---

## 🎨 Form Design Optimization

### Visual Hierarchy
1. **Hero Section**: "Enroll Your Child in NT STEM"
2. **Progress Indicator**: Show form progress (25%, 50%, 75%, 100%)
3. **Section Headers**: Clear section titles with icons
4. **Required Fields**: Mark with red asterisk (*)
5. **Help Text**: Add tooltips for complex fields

### Color Scheme
- **Primary Color**: #0066cc (Blue)
- **Secondary Color**: #ff6b35 (Orange)
- **Accent Color**: #00d9ff (Cyan)
- **Success Color**: #27ae60 (Green)
- **Error Color**: #e74c3c (Red)

### Mobile Optimization
- Single column layout on mobile
- Large touch targets (min 44px)
- Clear button labels
- Minimal scrolling between sections
- Mobile-friendly date picker

### Accessibility
- Proper label associations
- ARIA labels for screen readers
- Keyboard navigation support
- High contrast text
- Clear error messages

---

## 📊 Form Analytics to Track

### Key Metrics
1. **Form Completion Rate**: % of started forms that are submitted
2. **Drop-off Points**: Which sections have highest abandonment
3. **Time to Complete**: Average form completion time
4. **Most Popular Programs**: Which program type gets most bookings
5. **Peak Booking Times**: When do most bookings occur
6. **Conversion Rate**: Bookings per website visitor

### Optimization Actions Based on Data
- If drop-off high at Section 3: Simplify program selection
- If drop-off high at Section 6: Make health questions less intimidating
- If completion time > 10 min: Reduce number of fields
- If low conversion: Add testimonials or trust badges

---

## 🔐 Data Security & Privacy

### GDPR/Privacy Compliance
- Add privacy policy link
- Obtain explicit consent for marketing emails
- Secure data storage (JotForm handles this)
- Clear data retention policy
- Option to delete personal data

### Privacy Policy Statement
```
"We collect your information to process your booking and 
communicate about our programs. We will never share your 
data with third parties without consent. You can request 
to delete your data at any time by contacting us."
```

---

## 🚀 Advanced Features to Implement

### 1. Payment Integration
- Add Stripe or PayPal payment button
- Collect deposit (e.g., HK$200 to confirm booking)
- Send payment receipt automatically

### 2. Calendar Integration
- Show available class slots
- Prevent double-booking
- Auto-sync with your calendar system

### 3. Automated Follow-up
- Send reminder email 24 hours before class
- Send feedback survey after first class
- Send monthly newsletter to opted-in parents

### 4. SMS Notifications
- Send booking confirmation via SMS
- Send class reminders via SMS
- Send payment reminders via SMS

### 5. Referral Program
- Add referral code field
- Track referrals
- Offer discounts for referrals

---

## 📱 Contact Information to Display

### Email
- **Booking Inquiries**: contact@ntstem.hk
- **General Questions**: info@ntstem.hk
- **Complaints/Feedback**: feedback@ntstem.hk

### Phone
- **Main Line**: +852 1234 5678
- **WhatsApp**: +852 1234 5678 (preferred for quick responses)

### Response Time Targets
- Email: Within 24 hours
- WhatsApp: Within 2 hours (during business hours)
- Phone: Answer within 3 rings

---

## 👥 Tutor Information to Add

### For Each Tutor, Include:
- **Full Name**
- **Qualifications** (degrees, certifications)
- **Years of Experience**
- **Specializations** (e.g., Robotics, Architecture, Environmental Science)
- **Teaching Philosophy**
- **Languages Spoken**
- **Fun Fact** (to make them relatable)
- **Photo** (professional headshot)

### Example Tutor Bio Template:
```
[Tutor Name]
[Specialization]

[Tutor Name] has [X] years of experience teaching STEM 
to students aged [age range]. With a background in 
[relevant field], [he/she] brings real-world expertise 
to every class. [His/Her] students love [specific teaching 
style or approach]. When not teaching, [Tutor Name] enjoys 
[hobby related to STEM].

Qualifications:
- [Degree/Certification]
- [Degree/Certification]
- [Relevant Experience]
```

---

## ✅ Pre-Launch Checklist

- [ ] All form fields created and tested
- [ ] Conditional logic rules implemented and tested
- [ ] Email notifications configured
- [ ] Auto-calculation formulas working correctly
- [ ] Mobile responsiveness verified
- [ ] Accessibility tested (keyboard, screen reader)
- [ ] Privacy policy added
- [ ] Terms & conditions added
- [ ] Contact information verified
- [ ] Tutor bios complete with photos
- [ ] Form tested end-to-end
- [ ] Confirmation email tested
- [ ] Admin notification email tested
- [ ] Form embedded on website
- [ ] Analytics tracking enabled
- [ ] Backup system in place (export responses)

---

## 🔄 Ongoing Optimization

### Monthly Review
- Analyze form completion rates
- Review drop-off points
- Check for form errors or issues
- Update tutor information if needed
- Review customer feedback

### Quarterly Updates
- Update pricing if needed
- Add new program offerings
- Refresh testimonials
- Update tutor bios
- Analyze booking trends

### Annual Review
- Complete form redesign if needed
- Update curriculum highlights
- Refresh marketing messaging
- Analyze year-over-year growth
- Plan for next year's programs

---

## 📞 Support & Troubleshooting

### Common Issues & Solutions

**Issue**: Form not sending confirmation emails
- **Solution**: Check email settings in JotForm, verify email address is correct

**Issue**: Conditional logic not working
- **Solution**: Verify field names match exactly, check logic syntax

**Issue**: Mobile form looks broken
- **Solution**: Test on actual mobile device, adjust column widths, use JotForm's mobile preview

**Issue**: Calculations showing wrong values
- **Solution**: Check formula syntax, verify field types (number vs text)

**Issue**: Form taking too long to load
- **Solution**: Reduce number of fields, optimize images, enable lazy loading

---

## 📚 Additional Resources

- JotForm Documentation: https://www.jotform.com/help/
- JotForm Conditional Logic Guide: https://www.jotform.com/help/form-logic/
- JotForm Email Notifications: https://www.jotform.com/help/email-notifications/
- JotForm Calculations: https://www.jotform.com/help/calculations/
- JotForm Integrations: https://www.jotform.com/integrations/

---

**Last Updated**: May 2026
**Version**: 1.0
**Maintained By**: NT STEM Team
