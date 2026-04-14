"""Checkout and complete the order"""

import fastworkflow
from fastworkflow.train.generate_synthetic import generate_diverse_utterances
from pydantic import BaseModel, Field

from ...application.support_session import SupportSession


class Signature:
    """Complete the order and generate order summary"""

    class Input(BaseModel):
        contact_phone: str = Field(
            description="Customer's phone number for contact",
            examples=['9876543210', '+91 9876543210'],
            default=""
        )
        contact_email: str = Field(
            description="Customer's email for contact",
            examples=['customer@example.com', 'john.smith@bakery.com'],
            default=""
        )

    class Output(BaseModel):
        success: bool = Field(description="Whether checkout was successful")
        order_summary: str = Field(description="Complete order summary")

    plain_utterances = [
        "I'm ready to checkout",
        "proceed with my order",
        "complete my order",
        "I want to finalize this",
        "checkout please",
        "ready to place order",
    ]

    @staticmethod
    def generate_utterances(workflow: fastworkflow.Workflow, command_name: str) -> list[str]:
        """Generate training utterances for LLM-based intent matching"""
        return [
            command_name.split('/')[-1].lower().replace('_', ' ')
        ] + generate_diverse_utterances(Signature.plain_utterances, command_name)


class ResponseGenerator:
    """Process checkout and generate order summary"""

    def _process_command(self, workflow: fastworkflow.Workflow, input: Signature.Input) -> Signature.Output:
        session: SupportSession = workflow.command_context_for_response_generation

        if not session.cart:
            return Signature.Output(
                success=False,
                order_summary="❌ Your cart is empty. Please add items before checking out."
            )

        # Generate the order summary
        order_summary = session.get_checkout_summary()

        # Add contact information if provided
        if input.contact_phone or input.contact_email:
            order_summary += "\n\n**YOUR CONTACT INFORMATION:**\n"
            if input.contact_phone:
                order_summary += f"   📞 Phone: {input.contact_phone}\n"
            if input.contact_email:
                order_summary += f"   📧 Email: {input.contact_email}\n"

        # Clear the cart after checkout
        session.clear_cart()

        return Signature.Output(
            success=True,
            order_summary=order_summary
        )

    def __call__(
        self,
        workflow: fastworkflow.Workflow,
        command: str,
        command_parameters: Signature.Input
    ) -> fastworkflow.CommandOutput:
        """The framework will call this function to process the command"""
        output = self._process_command(workflow, command_parameters)

        return fastworkflow.CommandOutput(
            workflow_id=workflow.id,
            command_responses=[
                fastworkflow.CommandResponse(response=output.order_summary)
            ]
        )
