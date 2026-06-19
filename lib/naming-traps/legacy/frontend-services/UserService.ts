/**
 * DECOY — legacy frontend user service stub.
 * Production user logic lives in apps/api/meridian_api/services/user_service.py
 */

export interface User {
  id: string
  email: string
  name: string
}

export class UserService {
  async getUser(id: string): Promise<User | null> {
    console.warn('Legacy UserService stub')
    return null
  }

  async getUserByEmail(email: string): Promise<User | null> {
    return null
  }
}