import pandas as pd


#
# Read the Excel file into a pandas DataFrame
class read:
    def __init__(self):
        self.Dict = None

    def excelData(self):
        df = pd.read_excel("C:/Users/Anup/Downloads/Fastrack Fallsem 2023-24 Slot Timetable Ver 1.1.xlsx",
                           sheet_name='Sheet2')

        # Get the values of a specific column
        column_values = df['Clash Table'].values
        column_value_key = df['Slot'].values
        self.Dict = {}
        print("k")
        for i in range(len(column_values)):
            self.Dict[column_value_key[i]] = column_values[i].split("/")
        print(column_values)
        # return self.Dict
        print(self.Dict)

    def returnDict(self):
        # return {'A1+TA1+TAA1': ['A1', 'TA1', 'TAA1', 'L6', 'L16', 'L23', 'L24', 'L52'], 'A1+TA1': ['A1', 'TA1', 'L2', 'L16', 'L23', 'L24'], 'A1': ['A1', 'L6', 'L23', 'L24'], 'TA1': ['TA1', 'L16'], 'TAA1': ['TAA1', 'L52'], 'B1+TB1+TBB1': ['B1', 'TB1', 'TBB1', 'L5', 'L15', 'L21', 'L22', 'L38'], 'B1+TB1': ['B1', 'TB1', 'L5', 'L15', 'L21', 'L22'], 'B1': ['B1', 'L5', 'L21', 'L22'], 'TB1': ['TB1', 'L15'], 'TBB1': ['TBB1', 'L38'], 'C1+TC1+TCC1': ['C1', 'TC1', 'TCC1', 'L2', 'L7', 'L11', 'L17', 'L27'], 'C1+TC1': ['C1', 'TC1', 'L2', 'L7', 'L11', 'L17'], 'C1': ['C1', 'L2', 'L7'], 'TC1': ['TC1', 'L11'], 'TCC1': ['TCC1', 'L27'], 'D1+TD1+TDD1': ['D1', 'TD1', 'TDD1', 'L1', 'L8', 'L12', 'L18', 'L43'], 'D1+TD1': ['D1', 'TD1', 'L1', 'L8', 'L12', 'L18'], 'D1': ['D1', 'L1', 'L12', 'L18'], 'TD1': ['TD1', 'L8'], 'TDD1': ['TDD1', 'L43'], 'E1+TE1': ['E1', 'TE1', 'L4', 'L9', 'L14', 'L19'], 'E1': ['E1', 'L9', 'L14', '19'], 'TE1': ['TE1', 'L4'], 'F1+TF1': ['F1', 'TF1', 'L3', 'L10', 'L13', 'L20'], 'F1': ['F1', 'L3', 'L10', 'L13'], 'TF1': ['TF1', 'L20'], 'A2+TA2+TAA2': ['A2', 'TA2', 'TAA2', 'L20', 'L32', 'L46', 'L57', 'L58'], 'A2+TA2': ['A2', 'TA2', 'L32', 'L46', 'L57', 'L58'], 'A2': ['A2', 'L32', 'L57', 'L58'], 'TA2': ['TA2', 'L46'], 'TAA2': ['TAA2', 'L20'], 'B2+TB2+TBB2': ['B2', 'TB2', 'TBB2', 'L10', 'L31', 'L45', 'L55', 'L56'], 'B2+TB2': ['B2', 'TB2', 'L31', 'L45', 'L55', 'L56'], 'B2': ['B2', 'L31', 'L55', 'L56'], 'TB2': ['TB2', 'L45'], 'TBB2': ['TBB2', 'L10'], 'C2+TC2+TCC2': ['C2', 'TC2', 'TCC2', 'L3', 'L26', 'L33', 'L40', 'L49'], 'C2+TC2': ['C2', 'TC2', 'L26', 'L33', 'L40', 'L49'], 'C2': ['C2', 'L26', 'L33', 'L49'], 'TC2': ['TC2', 'L40'], 'TCC2': ['TCC2', 'L3'], 'D2+TD2+TDD2': ['D2', 'TD2', 'TDD2', 'L13', 'L25', 'L34', 'L39', 'L50'], 'D2+TD2': ['D2', 'TD2', 'L25', 'L34', 'L39', 'L50'], 'D2': ['D2', 'L25', 'L39', 'L50'], 'TD2': ['TD2', 'L34'], 'TDD2': ['TDD2', 'L13'], 'E2+TE2': ['E2', 'TE2', 'L28', 'L37', 'L44', 'L51'], 'E2': ['E2', 'L37', 'L44', 'L51'], 'TE2': ['TE2', 'L28'], 'F2+TF2': ['F2', 'TF2', 'L27', 'L38', 'L43', 'L52'], 'F2': ['F2', 'L27', 'L38', 'L43'], 'TF2': ['TF2', 'L52']}
        return {'A1+TA1+TAA1': ['A1', 'TA1', 'TAA1', 'L6', 'L16', 'L23', 'L24', 'L52'], 'A1+TA1': ['A1', 'TA1', 'L2', 'L16', 'L23', 'L24'],
                'B1+TB1+TBB1': ['B1', 'TB1', 'TBB1', 'L5', 'L15', 'L21', 'L22', 'L38'], 'B1+TB1': ['B1', 'TB1', 'L5', 'L15',
                'L21', 'L22'], 'B1': ['B1', 'L5', 'L21', 'L22'], 'TB1': ['TB1', 'L15'], 'TBB1': ['TBB1', 'L38'], 'C1+TC1+TCC1': ['C1', 'TC1', 'TCC1', 'L2', 'L7', 'L11', 'L17', 'L27'],
                'C1+TC1': ['C1', 'TC1', 'L2', 'L7', 'L11', 'L17'],'D1+TD1+TDD1': ['D1', 'TD1', 'TDD1', 'L1', 'L8', 'L12', 'L18', 'L43'], 'D1+TD1': ['D1', 'TD1', 'L1', 'L8', 'L12', 'L18'],
                'E1+TE1': ['E1', 'TE1', 'L4', 'L9', 'L14', 'L19'],
                'F1+TF1': ['F1', 'TF1', 'L3', 'L10', 'L13', 'L20'],'A2+TA2+TAA2': ['A2', 'TA2', 'TAA2', 'L20', 'L32', 'L46', 'L57', 'L58'], 'A2+TA2': ['A2', 'TA2', 'L32', 'L46', 'L57', 'L58'],
                'B2+TB2+TBB2': ['B2', 'TB2', 'TBB2', 'L10', 'L31', 'L45', 'L55', 'L56'],
                'B2+TB2': ['B2', 'TB2', 'L31', 'L45', 'L55', 'L56'],
                'C2+TC2+TCC2': ['C2', 'TC2', 'TCC2', 'L3', 'L26', 'L33', 'L40', 'L49'], 'C2+TC2': ['C2', 'TC2', 'L26', 'L33', 'L40', 'L49'],
                'D2+TD2+TDD2': ['D2', 'TD2', 'TDD2', 'L13', 'L25', 'L34', 'L39', 'L50'],
                'D2+TD2': ['D2', 'TD2', 'L25', 'L34', 'L39', 'L50'],
                'E2+TE2': ['E2', 'TE2', 'L28', 'L37', 'L44', 'L51'],'F2+TF2': ['F2', 'TF2', 'L27', 'L38', 'L43', 'L52'],
                }


#
# if __name__ == "__main__":
#     mod = read()
#     mod.excelData()
#
#     print(mod.returnDict())