# overview
container -> action -> reducer -> provider -> selector -> container
At a high level, data in Laminar flows from an Action, through a Reducer, to a Provider. It is stored there until accessed by a selector. An action represents any sort of event and may be dispatched with a payload. Any number of reducers may listen for this action and are the link between an action and a provider. A reducer receives the action payload and the previous provider state and returns the new provider state. This state gets saved in the provider (actually, in the AdsDataAtom. See Laminar Providers). Components may subscribe to changes in the provider with a selector or by converting the provider to a Flux store. A trigger reducer is used to update a provider state based on changes in another provider state.
## flux selectors
[flux selectors](https://our.internmc.facebook.com/intern/wiki/Ads_Interfaces_Eng/Codebase/Selectors/)
in practice, we generally use chains of selectors that read data, aggregate it, and/or perform operations on it (such as calculating tax or converting currency) before feeding it to a React container

## reference

    [AdsPETablePageProvider.toFluxSelector()
