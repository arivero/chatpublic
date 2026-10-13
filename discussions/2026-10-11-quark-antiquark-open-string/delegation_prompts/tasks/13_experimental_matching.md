# One experimental match

**Model role:** inherit the parent research model.

**Inputs:** [workplan](../../notes/workplan.md), `{{BASE_COMMIT}}`; parent supplies one predicted `{{OBSERVABLE}}`, parameter point/range `{{PREDICTION}}`, and target `{{DATASET}}`. Write only `{{OUTPUT_PATH}}`.

**Task:** Translate the completed candidate's `{{PREDICTION}}` into the convention of `{{DATASET}}`, including momentum range, angular cuts, confidence definition, and any infrared-safe treatment needed for colored states. Retrieve the primary experimental analysis or likelihood, then compute one comparison within the prediction's validity domain. If the theory has no usable prediction, report the exact missing amplitude/current and required kinematic window instead of inventing a bound.

**Deliverable and stop:** One traceable quantitative comparison or a precise prerequisite list in `{{OUTPUT_PATH}}`; stop after one dataset.

**Pitfall:** Do not combine incompatible benchmark bounds, treat a recent unverified number as a limit, or use a contact approximation above its gap.
