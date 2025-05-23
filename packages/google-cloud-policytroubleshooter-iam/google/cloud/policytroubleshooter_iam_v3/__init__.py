# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.policytroubleshooter_iam_v3 import gapic_version as package_version

__version__ = package_version.__version__


from .services.policy_troubleshooter import (
    PolicyTroubleshooterAsyncClient,
    PolicyTroubleshooterClient,
)
from .types.troubleshooter import (
    AccessTuple,
    AllowAccessState,
    AllowBindingExplanation,
    AllowPolicyExplanation,
    ConditionContext,
    ConditionExplanation,
    DenyAccessState,
    DenyPolicyExplanation,
    DenyRuleExplanation,
    ExplainedAllowPolicy,
    ExplainedDenyPolicy,
    ExplainedDenyResource,
    HeuristicRelevance,
    MembershipMatchingState,
    PermissionPatternMatchingState,
    RolePermissionInclusionState,
    TroubleshootIamPolicyRequest,
    TroubleshootIamPolicyResponse,
)

__all__ = (
    "PolicyTroubleshooterAsyncClient",
    "AccessTuple",
    "AllowAccessState",
    "AllowBindingExplanation",
    "AllowPolicyExplanation",
    "ConditionContext",
    "ConditionExplanation",
    "DenyAccessState",
    "DenyPolicyExplanation",
    "DenyRuleExplanation",
    "ExplainedAllowPolicy",
    "ExplainedDenyPolicy",
    "ExplainedDenyResource",
    "HeuristicRelevance",
    "MembershipMatchingState",
    "PermissionPatternMatchingState",
    "PolicyTroubleshooterClient",
    "RolePermissionInclusionState",
    "TroubleshootIamPolicyRequest",
    "TroubleshootIamPolicyResponse",
)
