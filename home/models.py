from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel


class HomePage(Page):
    about = RichTextField(blank=True)
    partners_blurb = RichTextField(blank=True)
    partners_list = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('about',classname='full'),
    	FieldPanel('partners_blurb',classname='full'),
    	FieldPanel('partners_list',classname='full'),
    ]


class AboutPage(Page):
    profile = RichTextField(blank=True)
    locations_blurb = RichTextField(blank=True)
    history = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('profile',classname='full'),
    	InlinePanel('government_clients',label='Government Clients'),
    	InlinePanel('dod_clients',label='DoD Clients'),
    	InlinePanel('commercial_clients',label='Commercial Clients'),
        FieldPanel('locations_blurb',classname='full'),
    	InlinePanel('office_locations',label='Offices'),
    	InlinePanel('awards',label='Awards'),
    	FieldPanel('history',classname='full'),
    ]

class AboutPageAwards(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='awards')
    award_name = models.CharField(blank=True, max_length=250)
    award_description = models.CharField(blank=True, max_length=280)

    panels = [
        FieldPanel('award_name'),
        FieldPanel('award_description'),
    ]


class AboutPageOffice(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='office_locations')
    office_name = models.CharField(blank=True, max_length=250)
    office_address = RichTextField(blank=True)
    office_phone = models.CharField(blank=True, max_length=16)
    office_fax = models.CharField(blank=True, max_length=16)

    panels = [
        FieldPanel('office_name'),
        FieldPanel('office_address'),
        FieldPanel('office_phone'),
        FieldPanel('office_fax'),
    ]


class AboutPageGovernmentClients(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='government_clients')
    client_name = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('client_name'),
    ]


class AboutPageDoDClients(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='dod_clients')
    client_name = models.CharField(blank=True, max_length=250)
    
    panels = [
        FieldPanel('client_name'),
    ]

class AboutPageCommercialClients(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='commercial_clients')
    client_name = models.CharField(blank=True, max_length=250)
    
    panels = [
        FieldPanel('client_name'),
    ]    


class ServicesPage(Page):
    approach = RichTextField(blank=True)
    personnel_blurb = RichTextField(blank=True)
    processes_blurb = RichTextField(blank=True)
    performance_blurb = RichTextField(blank=True)
    contract_vehicles_blurb = RichTextField(blank=True)
    contract_vehicles_list = RichTextField(blank=True)
    core_capabilities_list = RichTextField(blank=True)
    test_management_pastperf = RichTextField(blank=True)
    modeling_simulation_pastperf = RichTextField(blank=True)
    intel_pastperf = RichTextField(blank=True)
    cybersecurity_pastperf = RichTextField(blank=True)
    systems_analysis_eng_pastperf = RichTextField(blank=True)
    assistive_tech_pastperf = RichTextField(blank=True)
    document_management_pastperf = RichTextField(blank=True)
    distance_learning_pastperf = RichTextField(blank=True)
    technical_admin_pastperf = RichTextField(blank=True)
                            
    content_panels = Page.content_panels + [
    	FieldPanel('approach',classname='full'),
    	FieldPanel('personnel_blurb',classname='full'),
    	FieldPanel('processes_blurb',classname='full'),
    	FieldPanel('performance_blurb',classname='full'),
    	FieldPanel('contract_vehicles_blurb',classname='full'),
    	FieldPanel('contract_vehicles_list',classname='full'),
    	FieldPanel('core_capabilities_list',classname='full'),
    	FieldPanel('test_management_pastperf',classname='full'),
    	FieldPanel('modeling_simulation_pastperf',classname='full'),
    	FieldPanel('intel_pastperf',classname='full'),
    	FieldPanel('cybersecurity_pastperf',classname='full'),
    	FieldPanel('systems_analysis_eng_pastperf',classname='full'),
    	FieldPanel('assistive_tech_pastperf',classname='full'),
    	FieldPanel('document_management_pastperf',classname='full'),
    	FieldPanel('distance_learning_pastperf',classname='full'),
    	FieldPanel('technical_admin_pastperf',classname='full'),    	    	    	    	
    ]


class CareersPage(Page):
    join_us_blurb = RichTextField(blank=True)
    benefits_holidays_details = RichTextField(blank=True)
    benefits_holidaypay_details = RichTextField(blank=True)
    benefits_pto_details = RichTextField(blank=True)
    benefits_health_insurance_details = RichTextField(blank=True)
    benefits_disability_details = RichTextField(blank=True)
    benefits_retirement_details = RichTextField(blank=True)                                    

    content_panels = Page.content_panels + [
    	FieldPanel('join_us_blurb',classname='full'),
    	FieldPanel('benefits_holidays_details',classname='full'),
    	FieldPanel('benefits_holidaypay_details',classname='full'),
    	FieldPanel('benefits_pto_details',classname='full'),
    	FieldPanel('benefits_health_insurance_details',classname='full'),
    	FieldPanel('benefits_disability_details',classname='full'),
    	FieldPanel('benefits_retirement_details',classname='full'),
    ]


class ContactPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('bd_contacts',label='BD Contacts'),
        InlinePanel('hr_contacts',label='HR Contacts'),
        InlinePanel('contract_vehicle_contacts',label='Contract Vehicles Contacts'),
    	InlinePanel('general_contacts',label='General Contacts'),
    ]


class ContactPageBdContacts(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='bd_contacts')
    name = models.CharField(blank=True,max_length=250)
    title = models.CharField(blank=True,max_length=250)
    email = models.CharField(blank=True,max_length=250)
    phone = models.CharField(blank=True,max_length=250)
    fax = models.CharField(blank=True,max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('fax'),
    ]


class ContactPageHrContacts(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='hr_contacts')
    name = models.CharField(blank=True,max_length=250)
    title = models.CharField(blank=True,max_length=250)
    email = models.CharField(blank=True,max_length=250)
    phone = models.CharField(blank=True,max_length=250)
    fax = models.CharField(blank=True,max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('fax'),
    ]


class ContactPageContractVehicleContacts(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='contract_vehicle_contacts')
    name = models.CharField(blank=True,max_length=250)
    title = models.CharField(blank=True,max_length=250)
    email = models.CharField(blank=True,max_length=250)
    phone = models.CharField(blank=True,max_length=250)
    fax = models.CharField(blank=True,max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('fax'),
    ]


class ContactPageGeneralContacts(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='general_contacts')
    name = models.CharField(blank=True,max_length=250)
    title = models.CharField(blank=True,max_length=250)
    email = models.CharField(blank=True,max_length=250)
    phone = models.CharField(blank=True,max_length=250)
    fax = models.CharField(blank=True,max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('fax'),
    ]    


class CyberincubatorPage(Page):
    cyber_incubator_blurb = RichTextField(blank=True)
    program_overview = RichTextField(blank=True)
    participant_expectations = RichTextField(blank=True)
    program_benefits = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('cyber_incubator_blurb',classname='full'),
        FieldPanel('program_overview',classname='full'),
        FieldPanel('participant_expectations',classname='full'),
        FieldPanel('program_benefits',classname='full'),
        InlinePanel('cyberincubator_internship_descriptions',label='Internship Descriptions')
    ]


class CyberincubatorPageInternshipDescriptions(Orderable):
    page = ParentalKey(CyberincubatorPage, on_delete=models.CASCADE, related_name='cyberincubator_internship_descriptions')
    header = models.CharField(blank=True, max_length=250)
    description = models.TextField(blank=True, max_length=500)
    icon_code = models.CharField(blank=True, max_length=16)

    panels = [
        FieldPanel('header'),
        FieldPanel('icon_code'),
        FieldPanel('description'),
    ]