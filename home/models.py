from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    about = RichTextField(blank=True)
    partners_blurb = RichTextField(blank=True)
    partners_list = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('about',classname="full"),
    	FieldPanel('partners_blurb',classname="full"),
    	FieldPanel('partners_list',classname="full"),
    ]


class AboutPage(Page):
    profile = RichTextField(blank=True)
    government_clients = RichTextField(blank=True)
    dod_clients = RichTextField(blank=True)
    commercial_clients = RichTextField(blank=True)
    hq_name = RichTextField(blank=True)
    hq_details = RichTextField(blank=True)
    second_office_name = RichTextField(blank=True)
    second_office_details = RichTextField(blank=True)
    third_office_name = RichTextField(blank=True)
    third_office_details = RichTextField(blank=True)
    award_one_name = RichTextField(blank=True)
    award_one_details = RichTextField(blank=True)
    award_two_name = RichTextField(blank=True)
    award_two_details = RichTextField(blank=True)
    award_three_name = RichTextField(blank=True)
    award_three_details = RichTextField(blank=True)
    award_four_name = RichTextField(blank=True)
    award_four_details = RichTextField(blank=True)
    award_five_name = RichTextField(blank=True)
    award_five_details = RichTextField(blank=True)
    award_six_name = RichTextField(blank=True)
    award_six_details = RichTextField(blank=True)
    history = RichTextField(blank=True)                                                             

    content_panels = Page.content_panels + [
    	FieldPanel('profile',classname="full"),
    	FieldPanel('government_clients',classname="full"),
    	FieldPanel('dod_clients',classname="full"),
    	FieldPanel('commercial_clients',classname="full"),
    	FieldPanel('hq_name',classname="full"),
    	FieldPanel('hq_details',classname="full"),
    	FieldPanel('second_office_name',classname="full"),
    	FieldPanel('second_office_details',classname="full"),
    	FieldPanel('third_office_name',classname="full"),
    	FieldPanel('third_office_details',classname="full"),
    	FieldPanel('award_one_name',classname="full"),
    	FieldPanel('award_one_details',classname="full"),
    	FieldPanel('award_two_name',classname="full"),
    	FieldPanel('award_two_details',classname="full"),
    	FieldPanel('award_three_name',classname="full"),
    	FieldPanel('award_three_details',classname="full"),
    	FieldPanel('award_four_name',classname="full"),
    	FieldPanel('award_four_details',classname="full"),
    	FieldPanel('award_five_name',classname="full"),
    	FieldPanel('award_five_details',classname="full"),
    	FieldPanel('award_six_name',classname="full"),
    	FieldPanel('award_six_details',classname="full"),
    	FieldPanel('history',classname="full"),
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
    	FieldPanel('approach',classname="full"),
    	FieldPanel('personnel_blurb',classname="full"),
    	FieldPanel('processes_blurb',classname="full"),
    	FieldPanel('performance_blurb',classname="full"),
    	FieldPanel('contract_vehicles_blurb',classname="full"),
    	FieldPanel('contract_vehicles_list',classname="full"),
    	FieldPanel('core_capabilities_list',classname="full"),
    	FieldPanel('test_management_pastperf',classname="full"),
    	FieldPanel('modeling_simulation_pastperf',classname="full"),
    	FieldPanel('intel_pastperf',classname="full"),
    	FieldPanel('cybersecurity_pastperf',classname="full"),
    	FieldPanel('systems_analysis_eng_pastperf',classname="full"),
    	FieldPanel('assistive_tech_pastperf',classname="full"),
    	FieldPanel('document_management_pastperf',classname="full"),
    	FieldPanel('distance_learning_pastperf',classname="full"),
    	FieldPanel('technical_admin_pastperf',classname="full"),    	    	    	    	
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
    	FieldPanel('join_us_blurb',classname="full"),
    	FieldPanel('benefits_holidays_details',classname="full"),
    	FieldPanel('benefits_holidaypay_details',classname="full"),
    	FieldPanel('benefits_pto_details',classname="full"),
    	FieldPanel('benefits_health_insurance_details',classname="full"),
    	FieldPanel('benefits_disability_details',classname="full"),
    	FieldPanel('benefits_retirement_details',classname="full"),
    ]


class ContactPage(Page):
    bd_contacts = RichTextField(blank=True)
    contractvehicles_contacts = RichTextField(blank=True)
    hr_contacts = RichTextField(blank=True)
    general_contacts = RichTextField(blank=True)                                   

    content_panels = Page.content_panels + [
    	FieldPanel('bd_contacts',classname="full"),
    	FieldPanel('contractvehicles_contacts',classname="full"),
    	FieldPanel('hr_contacts',classname="full"),
    	FieldPanel('general_contacts',classname="full"),
    ]    