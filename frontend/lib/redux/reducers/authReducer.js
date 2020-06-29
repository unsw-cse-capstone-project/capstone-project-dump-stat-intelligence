import * as types from '../types';

const initialState = {
    isLoggedIn : false,
    uid : null,
    userInfo : {
        first : null,
        last  : null,
        email : null,
        phone : null
        
    }
}


export const authReducer = (state=initialState, action) => {
    switch (action.type) {
        case types.LOGIN:
            return {
                ...state,
                isLoggedIn : true,
                userInfo : {
                    ...action.userInfo
                }
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