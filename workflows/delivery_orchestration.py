from agents.poc_1_delivery.delivery_lead_agent import DeliveryLeadAgent


def run_delivery_flow(feature: str, use_search: bool = False):
    """Execute the full delivery workflow and return results and trace."""
    lead = DeliveryLeadAgent(use_search=use_search)
    results = lead.run(feature)
    return results, lead.trace
