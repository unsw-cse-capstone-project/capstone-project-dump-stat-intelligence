import * as types from '../types';

const initialState = {
    isLoggedIn : false,
    uid : null,
    nextPage : null,
    userInfo : {
        first : null,
        last  : null,
        email : null,
        phone : null
        
    }
}


export const authReducer = (state=initialState, action) => {
    switch (action.type) {
        case types.NEW_NEXT:
            console.log(action.next);
            return {
                ...state,
                nextPage : action.next
            }
        case types.CLEAR_NEXT:
            return {
                ...state,
                nextPage : null
            }
        case types.LOGIN:
            return {
                ...state,
                isLoggedIn : true,
                userInfo : {
                    ...action.userInfo
                },
                uid : action.uid
            }
        case types.LOGOUT:
            return {
                ...initialState,
                isLoggedIn : false
            }
        case types.UPDATE_DEETS:
            return {
                ...state,
                userInfo : {
                    ...action.userInfo
                }
            }
        default:
            return state
    }
} 