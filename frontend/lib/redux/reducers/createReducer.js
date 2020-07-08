import * as types from "../types";

const initialState = {
    title : null,
    id : null,
    cook_time : null,
    ingredients : [],
    method : []
}



export const createReducer = (state = initialState, action) => {
    switch (action.type) {
        case types.LOAD_CREATE:
            return {
                ...action.loaded
            }
        case types.CLEAR_CREATE:
            return {
                ...initialState
            }
    }
}